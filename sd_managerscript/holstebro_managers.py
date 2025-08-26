# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import asyncio

import structlog
from fastapi.encoders import jsonable_encoder
from more_itertools import one
from raclients.graph.client import PersistentGraphQLClient  # type: ignore
from ramodels.mo._shared import Validity  # type: ignore

from .filters import compute_expected_managers
from .filters import filter_managers
from .mo import get_leder_org_units
from .queries import QUERY_CURRENT_MANAGERS
from .terminate import terminate_manager
from .util import execute_mutator
from .util import query_graphql
from .util import query_org_unit

try:
    import zoneinfo
except ImportError:  # pragma: no cover
    from backports import zoneinfo  # type: ignore

DEFAULT_TZ = zoneinfo.ZoneInfo("Europe/Copenhagen")

logger = structlog.get_logger()


async def reconcile_leder_managers(gql_client: PersistentGraphQLClient):
    """
    Main entrypoint: reconciles all _leder managers.
    - Fetch all _leder org units with associations.
    - Filter to only valid managers based on active engagement in parent (handles led-adm).
    - Determine which managers need creation or termination.
    """
    # Step 1: Fetch and parse _leder units
    leder_units = await get_leder_org_units(gql_client)
    logger.info(f"Fetched {len(leder_units)} _leder units")

    # Step 2: Filter to latest valid association per unit
    filtered_units = await asyncio.gather(
        *(filter_managers(gql_client, ou) for ou in leder_units)
    )
    filtered_units = [ou for ou in filtered_units if ou.associations]

    # Step 3: Build the sets of managers that should exist
    managers_should_exist = await compute_expected_managers(filtered_units)

    # Step 4: Fetch all current managers globally
    current_managers_data = await query_graphql(gql_client, QUERY_CURRENT_MANAGERS, {})
    current_managers = {
        (
            manager["current"]["org_unit_uuid"],
            manager["current"]["employee_uuid"],
        ): manager["current"]["uuid"]
        for manager in current_managers_data["managers"]["objects"]
    }

    # Step 5: Compute managers to create and terminate
    to_create = managers_should_exist - set(current_managers.keys())
    to_terminate = [
        (key, manager_uuid)
        for key, manager_uuid in current_managers.items()
        if key not in managers_should_exist
    ]

    logger.info(f"Managers to create: {to_create}")
    logger.info(f"Managers to terminate: {to_terminate}")

    # Step 6: Apply changes
    # for org_emp in to_create:
    #     await create_manager_for_employee(org_emp)  # implement this
    #
    # for key, manager_uuid in to_terminate:
    #     await terminate_manager_for_employee(manager_uuid)  # implement this

    return {"to_create": to_create, "to_terminate": to_terminate}
