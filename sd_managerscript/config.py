# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

from fastramqpi.config import Settings as FastRAMQPISettings
from pydantic import BaseSettings
from pydantic import Field


class ManagerSyncSettings(BaseSettings):
    fastramqpi: FastRAMQPISettings = Field(
        default_factory=FastRAMQPISettings, description="FastRAMQPI settings"
    )
    root_uuid: UUID = Field(description="UUID of the root org-unit")
    manager_type_uuid: UUID = Field(
        description="UUID defining manager type. Same for all managers"
    )
    responsibility_uuid: UUID = Field(
        description="UUID defining responsibility. Same for all managers"
    )
    manager_level_mapping: dict[UUID, UUID] = Field(
        description="Mapping dict from org-unit level to manager level"
    )

    class Config:
        env_nested_delimiter = "__"


def get_settings(*args, **kwargs) -> ManagerSyncSettings:
    return ManagerSyncSettings(*args, **kwargs)
