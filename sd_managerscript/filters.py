# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import asyncio
from datetime import datetime
from typing import Optional
from uuid import UUID

import structlog
from fastapi.encoders import jsonable_encoder
from more_itertools import one
from raclients.graph.client import PersistentGraphQLClient  # type: ignore

from .exceptions import ConflictingManagers
from .models import Association
from .models import OrgUnitManagers
from .queries import QUERY_ENGAGEMENTS
from .terminate import terminate_association
from .util import query_graphql

logger = structlog.get_logger()


async def filter_managers(
    gql_client: PersistentGraphQLClient, org_unit: OrgUnitManagers
) -> OrgUnitManagers:
    """
    Keep only the valid association for this _leder unit (latest engagement in parent).
    Terminate redundant associations.
    """
    associations = org_unit.associations
    if not associations:
        return org_unit

    # Get latest valid association (with active engagement in parent)
    latest_assoc = await pick_latest_valid_association(gql_client, org_unit)

    # TODO: Først terminér når scriptet er "færdigt", dvs. ikke terminer midt i det hele - hvis noget går galt skal der ikke termineres.
    if not latest_assoc:
        # Terminate all associations
        for assoc in associations:
            await terminate_association(gql_client, assoc.uuid)
        org_unit.associations = []
        return org_unit

    # Terminate others
    for assoc in associations:
        if assoc != latest_assoc:
            await terminate_association(gql_client, assoc.uuid)

    org_unit.associations = [latest_assoc]
    return org_unit


async def compute_expected_managers(
    filtered_units: list[OrgUnitManagers],
) -> set[tuple[str, str]]:
    """
    Compute the set of managers that should exist based on already-filtered associations.
    Applies led-adm logic.
    """
    managers_should_exist: set[tuple[str, str]] = set()

    for ou in filtered_units:
        if not ou.associations or not ou.parent:
            continue

        keep = one(ou.associations)  # already filtered
        parent = ou.parent
        employee_uuid = str(keep.employee_uuid)

        # Always add parent
        managers_should_exist.add((str(parent.uuid), employee_uuid))

        # led-adm → also add grandparent
        if parent.name.lower().endswith("led-adm") and parent.parent_uuid:
            managers_should_exist.add((str(parent.parent_uuid), employee_uuid))

    return managers_should_exist


async def pick_latest_valid_association(
    gql_client: PersistentGraphQLClient, org_unit: OrgUnitManagers
) -> Association | None:
    """
    From all associations in a _leder unit, pick the employee with the latest active engagement in the parent org unit.
    Terminates redundant associations if necessary.
    Returns the association to keep, or None if none are valid.
    """
    if not org_unit.associations or not org_unit.parent:
        return None

    parent_uuid = org_unit.parent.uuid
    associations = org_unit.associations

    # Fetch latest engagement dates for all associations
    engagement_dates = await asyncio.gather(
        *[
            get_latest_parent_engagement_from(
                gql_client, assoc.employee_uuid, parent_uuid
            )
            for assoc in associations
        ]
    )

    # Pair associations with their engagement date
    valid_pairs = [
        (assoc, dt)
        for assoc, dt in zip(associations, engagement_dates)
        if dt is not None
    ]

    if not valid_pairs:
        return None

    # Find the latest engagement date
    latest_date = max(dt for _, dt in valid_pairs)
    # TODO: Rename
    winners = [assoc for assoc, dt in valid_pairs if dt == latest_date]

    if len(winners) > 1:
        raise ConflictingManagers(
            f"Multiple employees share latest engagement date in _leder {org_unit.uuid}"
        )

    return one(winners)


async def get_latest_parent_engagement_from(
    gql_client: PersistentGraphQLClient, employee_uuid: UUID, parent_uuid: UUID
) -> datetime | None:
    """
    Return the latest engagement 'from' date for the employee in the given parent org unit.

    Args:
        gql_client: GraphQL client
        employee_uuid: UUID of the employee
        parent_uuid: UUID of the parent org unit to filter engagements

    Returns:
        datetime of latest engagement 'from' in parent org unit, or None if no valid engagement
    """
    # TODO: Giver det mening at hente alle engagementer ud for enheden?
    variables = {"uuid": str(employee_uuid)}
    data = await query_graphql(gql_client, QUERY_ENGAGEMENTS, variables)
    objs = data.get("engagements", {}).get("objects", [])

    latest: datetime | None = None

    for eng in objs:
        for validity in eng.get("validities", []):
            if validity.get("org_unit_uuid") != str(parent_uuid):
                continue
            from_date = validity.get("validity", {}).get("from")
            if from_date:
                dt = datetime.fromisoformat(from_date)
                if latest is None or dt > latest:
                    latest = dt

    return latest
