from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class RootManagerEngagements(BaseModel):
    org_units: "RootManagerEngagementsOrgUnits"


class RootManagerEngagementsOrgUnits(BaseModel):
    objects: list["RootManagerEngagementsOrgUnitsObjects"]


class RootManagerEngagementsOrgUnitsObjects(BaseModel):
    validities: list["RootManagerEngagementsOrgUnitsObjectsValidities"]


class RootManagerEngagementsOrgUnitsObjectsValidities(BaseModel):
    uuid: UUID
    has_children: bool
    managers: list["RootManagerEngagementsOrgUnitsObjectsValiditiesManagers"]


class RootManagerEngagementsOrgUnitsObjectsValiditiesManagers(BaseModel):
    uuid: UUID
    employee: (
        None | (list["RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployee"])
    )


class RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployee(BaseModel):
    engagements: list[
        "RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagements"
    ]


class RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagements(
    BaseModel
):
    org_unit: list[
        "RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnit"
    ]
    validity: "RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsValidity"


class RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnit(
    BaseModel
):
    name: str
    uuid: UUID
    parent: Optional[
        "RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnitParent"
    ]


class RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnitParent(
    BaseModel
):
    name: str
    uuid: UUID


class RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsValidity(
    BaseModel
):
    from_: datetime = Field(alias="from")
    to: datetime | None


RootManagerEngagements.update_forward_refs()
RootManagerEngagementsOrgUnits.update_forward_refs()
RootManagerEngagementsOrgUnitsObjects.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValidities.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValiditiesManagers.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployee.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagements.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnit.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsOrgUnitParent.update_forward_refs()
RootManagerEngagementsOrgUnitsObjectsValiditiesManagersEmployeeEngagementsValidity.update_forward_refs()
