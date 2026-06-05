from pydantic import BaseModel


class ChannelSchema(BaseModel):
    workspace_id: int

class MessageSchema(BaseModel):
    text: str
    author_id: int