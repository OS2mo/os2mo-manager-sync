from uuid import UUID

from .base_model import BaseModel


class TerminateManager(BaseModel):
    manager_terminate: "TerminateManagerManagerTerminate"


class TerminateManagerManagerTerminate(BaseModel):
    uuid: UUID


TerminateManager.update_forward_refs()
TerminateManagerManagerTerminate.update_forward_refs()
