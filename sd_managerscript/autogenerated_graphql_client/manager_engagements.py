from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class ManagerEngagements(BaseModel):
    org_units: "ManagerEngagementsOrgUnits"


class ManagerEngagementsOrgUnits(BaseModel):
    objects: list["ManagerEngagementsOrgUnitsObjects"]


class ManagerEngagementsOrgUnitsObjects(BaseModel):
    validities: list["ManagerEngagementsOrgUnitsObjectsValidities"]


class ManagerEngagementsOrgUnitsObjectsValidities(BaseModel):
    uuid: UUID
    has_children: bool
    managers: list["ManagerEngagementsOrgUnitsObjectsValiditiesManagers"]


class ManagerEngagementsOrgUnitsObjectsValiditiesManagers(BaseModel):
    uuid: UUID
    employee: (
        None | (list["ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployee"])
    )


class ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployee(BaseModel):
    engagements: list[
        "ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagements"
    ]


class ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagements(BaseModel):
    org_unit: list[
        "ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnit"
    ]
    validity: (
        "ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsValidity"
    )


class ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnit(
    BaseModel
):
    name: str
    uuid: UUID
    parent: Optional[
        "ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnitParent"
    ]


class ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnitParent(
    BaseModel
):
    name: str
    uuid: UUID


class ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsValidity(
    BaseModel
):
    from_: datetime = Field(alias="from")
    to: datetime | None


ManagerEngagements.update_forward_refs()
ManagerEngagementsOrgUnits.update_forward_refs()
ManagerEngagementsOrgUnitsObjects.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValidities.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValiditiesManagers.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployee.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagements.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnit.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnitParent.update_forward_refs()
ManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsValidity.update_forward_refs()
