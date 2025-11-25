from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class TestingGetManagers(BaseModel):
    managers: "TestingGetManagersManagers"


class TestingGetManagersManagers(BaseModel):
    objects: list["TestingGetManagersManagersObjects"]


class TestingGetManagersManagersObjects(BaseModel):
    current: Optional["TestingGetManagersManagersObjectsCurrent"]


class TestingGetManagersManagersObjectsCurrent(BaseModel):
    org_unit_uuid: UUID
    employee_uuid: UUID | None


TestingGetManagers.update_forward_refs()
TestingGetManagersManagers.update_forward_refs()
TestingGetManagersManagersObjects.update_forward_refs()
TestingGetManagersManagersObjectsCurrent.update_forward_refs()
