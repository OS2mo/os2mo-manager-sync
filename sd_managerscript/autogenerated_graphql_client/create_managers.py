from uuid import UUID

from .base_model import BaseModel


class CreateManagers(BaseModel):
    managers_create: list["CreateManagersManagersCreate"]


class CreateManagersManagersCreate(BaseModel):
    uuid: UUID


CreateManagers.update_forward_refs()
CreateManagersManagersCreate.update_forward_refs()
