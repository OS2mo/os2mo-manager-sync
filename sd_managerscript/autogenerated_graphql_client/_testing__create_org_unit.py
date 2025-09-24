from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class TestingCreateOrgUnit(BaseModel):
    org_unit_create: "TestingCreateOrgUnitOrgUnitCreate"


class TestingCreateOrgUnitOrgUnitCreate(BaseModel):
    uuid: UUID
    current: Optional["TestingCreateOrgUnitOrgUnitCreateCurrent"]


class TestingCreateOrgUnitOrgUnitCreateCurrent(BaseModel):
    org_unit_level_uuid: UUID | None


TestingCreateOrgUnit.update_forward_refs()
TestingCreateOrgUnitOrgUnitCreate.update_forward_refs()
TestingCreateOrgUnitOrgUnitCreateCurrent.update_forward_refs()
