from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class TestingGetLederOrgUnitAssociations(BaseModel):
    org_units: "TestingGetLederOrgUnitAssociationsOrgUnits"


class TestingGetLederOrgUnitAssociationsOrgUnits(BaseModel):
    objects: list["TestingGetLederOrgUnitAssociationsOrgUnitsObjects"]


class TestingGetLederOrgUnitAssociationsOrgUnitsObjects(BaseModel):
    validities: list["TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValidities"]


class TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValidities(BaseModel):
    uuid: UUID
    name: str
    associations: list[
        "TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesAssociations"
    ]
    parent: Optional[
        "TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesParent"
    ]


class TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesAssociations(
    BaseModel
):
    uuid: UUID
    employee_uuid: UUID | None
    org_unit_uuid: UUID
    association_type_uuid: UUID | None
    validity: "TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesAssociationsValidity"


class TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesAssociationsValidity(
    BaseModel
):
    from_: datetime = Field(alias="from")
    to: datetime | None


class TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesParent(BaseModel):
    uuid: UUID
    name: str
    parent_uuid: UUID | None
    org_unit_level_uuid: UUID | None


TestingGetLederOrgUnitAssociations.update_forward_refs()
TestingGetLederOrgUnitAssociationsOrgUnits.update_forward_refs()
TestingGetLederOrgUnitAssociationsOrgUnitsObjects.update_forward_refs()
TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValidities.update_forward_refs()
TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesAssociations.update_forward_refs()
TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesAssociationsValidity.update_forward_refs()
TestingGetLederOrgUnitAssociationsOrgUnitsObjectsValiditiesParent.update_forward_refs()
