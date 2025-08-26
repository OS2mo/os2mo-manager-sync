# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from datetime import datetime
from uuid import UUID

import structlog
from raclients.graph.client import PersistentGraphQLClient  # type: ignore
from ramodels.mo._shared import Validity  # type: ignore

from .models import Association
from .models import EngagementFrom
from .models import OrgUnitManagers
from .models import Parent
from .queries import QUERY_ENGAGEMENTS
from .queries import QUERY_LEDER_ORG_UNITS
from .util import query_graphql

logger = structlog.get_logger()


async def get_leder_org_units(
    gql_client: PersistentGraphQLClient,
) -> list[OrgUnitManagers]:
    """
    Fetch all _leder org units with associations and convert them into OrgUnitManagers models.
    """

    data = await query_graphql(gql_client, QUERY_LEDER_ORG_UNITS, {})
    leder_units: list[OrgUnitManagers] = []

    for ou in data["org_units"]["objects"]:
        for validity in ou.get("validities", []):
            if (
                not validity.get("associations")
                or not validity["name"].lower().strip().endswith("_leder")
                or validity["name"].lower().strip().startswith("Ø_")
            ):
                continue

            try:
                obj_dict = {
                    "uuid": UUID(validity["uuid"]),
                    "name": validity["name"],
                    "associations": [
                        Association(
                            uuid=UUID(a["uuid"]),
                            org_unit_uuid=UUID(a["org_unit_uuid"]),
                            employee_uuid=UUID(a["employee_uuid"]),
                            association_type_uuid=UUID(a["association_type_uuid"]),
                            validity=Validity(
                                from_date=a["validity"]["from"],
                                to_date=a["validity"]["to"],
                            ),
                        )
                        for a in validity["associations"]
                    ],
                    "parent": Parent(
                        uuid=UUID(validity["parent"]["uuid"]),
                        name=validity["parent"]["name"],
                        parent_uuid=UUID(validity["parent"]["parent_uuid"])
                        if validity["parent"].get("parent_uuid")
                        else None,
                        org_unit_level_uuid=validity["parent"].get(
                            "org_unit_level_uuid"
                        ),
                    )
                    if validity.get("parent")
                    else None,
                }

                leder_units.append(OrgUnitManagers.parse_obj(obj_dict))
            except Exception as e:
                logger.warning(f"Skipping invalid org unit {validity.get('uuid')}: {e}")

    return leder_units


async def get_active_engagements(
    gql_client: PersistentGraphQLClient, employee_uuid: UUID
) -> EngagementFrom:
    """
    Checks the manager has an active engagement and returns the latest, if any.

    Args:
        gql_client: GraphQL client
        employee_uuid: UUID for the employee we want to fetch engagements for.
    Returns:
        dict: dict with employee uuid and engagement from date.

    """

    variables = {"uuid": employee_uuid}
    engagements = await query_graphql(gql_client, QUERY_ENGAGEMENTS, variables)
    logger.debug("Engagements fetched.", response=engagements)
    latest_from_date = None

    if engagements["engagements"]["objects"]:
        latest_from_date = max(
            datetime.fromisoformat(validity["validity"]["from"])
            for eng in engagements["engagements"]["objects"]
            for validity in eng["validities"]
        )
    return EngagementFrom(employee_uuid=employee_uuid, engagement_from=latest_from_date)
