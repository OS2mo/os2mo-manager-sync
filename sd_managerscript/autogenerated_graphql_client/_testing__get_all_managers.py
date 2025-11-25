from typing import Optional
from uuid import UUID

from .base_model import BaseModel


class TestingGetAllManagers(BaseModel):
    managers: "TestingGetAllManagersManagers"


class TestingGetAllManagersManagers(BaseModel):
    objects: list["TestingGetAllManagersManagersObjects"]


class TestingGetAllManagersManagersObjects(BaseModel):
    current: Optional["TestingGetAllManagersManagersObjectsCurrent"]


class TestingGetAllManagersManagersObjectsCurrent(BaseModel):
    uuid: UUID


TestingGetAllManagers.update_forward_refs()
TestingGetAllManagersManagers.update_forward_refs()
TestingGetAllManagersManagersObjects.update_forward_refs()
TestingGetAllManagersManagersObjectsCurrent.update_forward_refs()
