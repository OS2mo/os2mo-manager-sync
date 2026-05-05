from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class TestingGetOrgUnitManager(BaseModel):
    managers: "TestingGetOrgUnitManagerManagers"


class TestingGetOrgUnitManagerManagers(BaseModel):
    objects: list["TestingGetOrgUnitManagerManagersObjects"]


class TestingGetOrgUnitManagerManagersObjects(BaseModel):
    current: Optional["TestingGetOrgUnitManagerManagersObjectsCurrent"]


class TestingGetOrgUnitManagerManagersObjectsCurrent(BaseModel):
    org_unit_uuid: UUID
    employee_uuid: UUID | None


TestingGetOrgUnitManager.update_forward_refs()
TestingGetOrgUnitManagerManagers.update_forward_refs()
TestingGetOrgUnitManagerManagersObjects.update_forward_refs()
TestingGetOrgUnitManagerManagersObjectsCurrent.update_forward_refs()
