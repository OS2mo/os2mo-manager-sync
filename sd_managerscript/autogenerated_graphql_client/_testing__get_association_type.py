from uuid import UUID

from .base_model import BaseModel


class TestingGetAssociationType(BaseModel):
    classes: "TestingGetAssociationTypeClasses"


class TestingGetAssociationTypeClasses(BaseModel):
    objects: list["TestingGetAssociationTypeClassesObjects"]


class TestingGetAssociationTypeClassesObjects(BaseModel):
    uuid: UUID


TestingGetAssociationType.update_forward_refs()
TestingGetAssociationTypeClasses.update_forward_refs()
TestingGetAssociationTypeClassesObjects.update_forward_refs()
