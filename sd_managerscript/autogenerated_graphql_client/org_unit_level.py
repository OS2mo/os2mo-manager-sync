from typing import List
from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class OrgUnitLevel(BaseModel):
    org_units: "OrgUnitLevelOrgUnits"


class OrgUnitLevelOrgUnits(BaseModel):
    objects: List["OrgUnitLevelOrgUnitsObjects"]


class OrgUnitLevelOrgUnitsObjects(BaseModel):
    validities: List["OrgUnitLevelOrgUnitsObjectsValidities"]


class OrgUnitLevelOrgUnitsObjectsValidities(BaseModel):
    uuid: UUID
    name: str
    org_unit_level_uuid: Optional[UUID]
    parent: Optional["OrgUnitLevelOrgUnitsObjectsValiditiesParent"]


class OrgUnitLevelOrgUnitsObjectsValiditiesParent(BaseModel):
    uuid: UUID
    org_unit_level_uuid: Optional[UUID]


OrgUnitLevel.update_forward_refs()
OrgUnitLevelOrgUnits.update_forward_refs()
OrgUnitLevelOrgUnitsObjects.update_forward_refs()
OrgUnitLevelOrgUnitsObjectsValidities.update_forward_refs()
OrgUnitLevelOrgUnitsObjectsValiditiesParent.update_forward_refs()
