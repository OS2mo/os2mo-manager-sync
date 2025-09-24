from uuid import UUID

from .base_model import BaseModel


class TestingGetOrgUnitLevel(BaseModel):
    classes: "TestingGetOrgUnitLevelClasses"


class TestingGetOrgUnitLevelClasses(BaseModel):
    objects: list["TestingGetOrgUnitLevelClassesObjects"]


class TestingGetOrgUnitLevelClassesObjects(BaseModel):
    uuid: UUID


TestingGetOrgUnitLevel.update_forward_refs()
TestingGetOrgUnitLevelClasses.update_forward_refs()
TestingGetOrgUnitLevelClassesObjects.update_forward_refs()
