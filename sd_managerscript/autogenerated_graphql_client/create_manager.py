from uuid import UUID

from .base_model import BaseModel


class CreateManager(BaseModel):
    manager_create: "CreateManagerManagerCreate"


class CreateManagerManagerCreate(BaseModel):
    uuid: UUID


CreateManager.update_forward_refs()
CreateManagerManagerCreate.update_forward_refs()
