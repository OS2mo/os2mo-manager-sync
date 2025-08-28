from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class LederOrgUnits(BaseModel):
    org_units: "LederOrgUnitsOrgUnits"


class LederOrgUnitsOrgUnits(BaseModel):
    objects: list["LederOrgUnitsOrgUnitsObjects"]


class LederOrgUnitsOrgUnitsObjects(BaseModel):
    validities: list["LederOrgUnitsOrgUnitsObjectsValidities"]


class LederOrgUnitsOrgUnitsObjectsValidities(BaseModel):
    uuid: UUID
    name: str
    associations: list["LederOrgUnitsOrgUnitsObjectsValiditiesAssociations"]
    parent: Optional["LederOrgUnitsOrgUnitsObjectsValiditiesParent"]


class LederOrgUnitsOrgUnitsObjectsValiditiesAssociations(BaseModel):
    uuid: UUID
    employee_uuid: UUID | None
    org_unit_uuid: UUID
    association_type_uuid: UUID | None
    validity: "LederOrgUnitsOrgUnitsObjectsValiditiesAssociationsValidity"


class LederOrgUnitsOrgUnitsObjectsValiditiesAssociationsValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: datetime | None


class LederOrgUnitsOrgUnitsObjectsValiditiesParent(BaseModel):
    uuid: UUID
    name: str
    parent_uuid: UUID | None
    org_unit_level_uuid: UUID | None


LederOrgUnits.update_forward_refs()
LederOrgUnitsOrgUnits.update_forward_refs()
LederOrgUnitsOrgUnitsObjects.update_forward_refs()
LederOrgUnitsOrgUnitsObjectsValidities.update_forward_refs()
LederOrgUnitsOrgUnitsObjectsValiditiesAssociations.update_forward_refs()
LederOrgUnitsOrgUnitsObjectsValiditiesAssociationsValidity.update_forward_refs()
LederOrgUnitsOrgUnitsObjectsValiditiesParent.update_forward_refs()
