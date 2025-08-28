from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class CurrentManagers(BaseModel):
    managers: "CurrentManagersManagers"


class CurrentManagersManagers(BaseModel):
    objects: list["CurrentManagersManagersObjects"]


class CurrentManagersManagersObjects(BaseModel):
    current: Optional["CurrentManagersManagersObjectsCurrent"]


class CurrentManagersManagersObjectsCurrent(BaseModel):
    uuid: UUID
    employee_uuid: UUID | None
    org_unit_uuid: UUID


CurrentManagers.update_forward_refs()
CurrentManagersManagers.update_forward_refs()
CurrentManagersManagersObjects.update_forward_refs()
CurrentManagersManagersObjectsCurrent.update_forward_refs()
