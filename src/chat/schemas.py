from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.workspaces.schemas import MemberCreateSchema


class MessageSchema(BaseModel):
    text: str
    author_id: int
    workspace_id: int

class MessageResponseSchema(BaseModel):
    text: str
    author: MemberCreateSchema
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)