# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from unittest.mock import AsyncMock
from uuid import uuid4

from sd_managerscript.init import get_organisation, get_facet_uuid


async def test_get_organisation():
    # Arrange
    org_uuid = uuid4()
    mock_gql_client = AsyncMock()
    mock_gql_client.execute.return_value = {"org": {"uuid": str(org_uuid)}}

    # Act
    _uuid = await get_organisation(mock_gql_client)

    # Assert
    assert _uuid == org_uuid


async def test_get_facet_uuid():
    # Arrange
    facet_uuid = uuid4()
    mock_gql_client = AsyncMock()
    mock_gql_client.execute.return_value = {
        "facets": [{"uuid": str(facet_uuid)}]
    }
    # Act
    _uuid = await get_facet_uuid(mock_gql_client, "manager_level")

    # Assert
    assert _uuid == facet_uuid
