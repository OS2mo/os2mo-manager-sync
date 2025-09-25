from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class OrgUnitLevel(BaseModel):
    org_units: "OrgUnitLevelOrgUnits"


class OrgUnitLevelOrgUnits(BaseModel):
    objects: list["OrgUnitLevelOrgUnitsObjects"]


class OrgUnitLevelOrgUnitsObjects(BaseModel):
    validities: list["OrgUnitLevelOrgUnitsObjectsValidities"]


class OrgUnitLevelOrgUnitsObjectsValidities(BaseModel):
    uuid: UUID
    name: str
    org_unit_level: Optional["OrgUnitLevelOrgUnitsObjectsValiditiesOrgUnitLevel"]
    parent: Optional["OrgUnitLevelOrgUnitsObjectsValiditiesParent"]


class OrgUnitLevelOrgUnitsObjectsValiditiesOrgUnitLevel(BaseModel):
    user_key: str


class OrgUnitLevelOrgUnitsObjectsValiditiesParent(BaseModel):
    uuid: UUID
    org_unit_level: Optional["OrgUnitLevelOrgUnitsObjectsValiditiesParentOrgUnitLevel"]


class OrgUnitLevelOrgUnitsObjectsValiditiesParentOrgUnitLevel(BaseModel):
    user_key: str


OrgUnitLevel.update_forward_refs()
OrgUnitLevelOrgUnits.update_forward_refs()
OrgUnitLevelOrgUnitsObjects.update_forward_refs()
OrgUnitLevelOrgUnitsObjectsValidities.update_forward_refs()
OrgUnitLevelOrgUnitsObjectsValiditiesOrgUnitLevel.update_forward_refs()
OrgUnitLevelOrgUnitsObjectsValiditiesParent.update_forward_refs()
OrgUnitLevelOrgUnitsObjectsValiditiesParentOrgUnitLevel.update_forward_refs()
