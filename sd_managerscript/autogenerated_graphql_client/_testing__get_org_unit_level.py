from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class TestingGetOrgUnitLevel(BaseModel):
    classes: "TestingGetOrgUnitLevelClasses"


class TestingGetOrgUnitLevelClasses(BaseModel):
    objects: list["TestingGetOrgUnitLevelClassesObjects"]


class TestingGetOrgUnitLevelClassesObjects(BaseModel):
    uuid: UUID
    current: Optional["TestingGetOrgUnitLevelClassesObjectsCurrent"]


class TestingGetOrgUnitLevelClassesObjectsCurrent(BaseModel):
    user_key: str


TestingGetOrgUnitLevel.update_forward_refs()
TestingGetOrgUnitLevelClasses.update_forward_refs()
TestingGetOrgUnitLevelClassesObjects.update_forward_refs()
TestingGetOrgUnitLevelClassesObjectsCurrent.update_forward_refs()
