from uuid import UUID

from .base_model import BaseModel


class TestingGetEngagementType(BaseModel):
    classes: "TestingGetEngagementTypeClasses"


class TestingGetEngagementTypeClasses(BaseModel):
    objects: list["TestingGetEngagementTypeClassesObjects"]


class TestingGetEngagementTypeClassesObjects(BaseModel):
    uuid: UUID


TestingGetEngagementType.update_forward_refs()
TestingGetEngagementTypeClasses.update_forward_refs()
TestingGetEngagementTypeClassesObjects.update_forward_refs()
