from datetime import datetime
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class Engagements(BaseModel):
    engagements: "EngagementsEngagements"


class EngagementsEngagements(BaseModel):
    objects: list["EngagementsEngagementsObjects"]


class EngagementsEngagementsObjects(BaseModel):
    validities: list["EngagementsEngagementsObjectsValidities"]


class EngagementsEngagementsObjectsValidities(BaseModel):
    org_unit_uuid: UUID
    validity: "EngagementsEngagementsObjectsValiditiesValidity"


class EngagementsEngagementsObjectsValiditiesValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: datetime | None


Engagements.update_forward_refs()
EngagementsEngagements.update_forward_refs()
EngagementsEngagementsObjects.update_forward_refs()
EngagementsEngagementsObjectsValidities.update_forward_refs()
EngagementsEngagementsObjectsValiditiesValidity.update_forward_refs()
