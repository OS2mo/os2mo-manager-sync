from uuid import UUID

from .base_model import BaseModel


class TestingGetManagerLevelByUserKey(BaseModel):
    classes: "TestingGetManagerLevelByUserKeyClasses"


class TestingGetManagerLevelByUserKeyClasses(BaseModel):
    objects: list["TestingGetManagerLevelByUserKeyClassesObjects"]


class TestingGetManagerLevelByUserKeyClassesObjects(BaseModel):
    uuid: UUID


TestingGetManagerLevelByUserKey.update_forward_refs()
TestingGetManagerLevelByUserKeyClasses.update_forward_refs()
TestingGetManagerLevelByUserKeyClassesObjects.update_forward_refs()
