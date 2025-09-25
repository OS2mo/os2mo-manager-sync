from uuid import UUID

from .base_model import BaseModel


class ManagerLevel(BaseModel):
    classes: "ManagerLevelClasses"


class ManagerLevelClasses(BaseModel):
    objects: list["ManagerLevelClassesObjects"]


class ManagerLevelClassesObjects(BaseModel):
    validities: list["ManagerLevelClassesObjectsValidities"]


class ManagerLevelClassesObjectsValidities(BaseModel):
    uuid: UUID


ManagerLevel.update_forward_refs()
ManagerLevelClasses.update_forward_refs()
ManagerLevelClassesObjects.update_forward_refs()
ManagerLevelClassesObjectsValidities.update_forward_refs()
