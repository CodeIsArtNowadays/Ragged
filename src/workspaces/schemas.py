from typing import List
from pydantic import BaseModel, ConfigDict

from src.core.custom_types import RoleLiteral


class MemberCreateSchema(BaseModel):
    user_id: int
    username: str

    model_config = ConfigDict(from_attributes=True) 


class WorkspaceBaseSchema(BaseModel):
    title: str

    model_config = ConfigDict(from_attributes=True)


class WorkspaceListSchema(WorkspaceBaseSchema):
    id: int


class WorkspaceCreateRequestSchema(WorkspaceBaseSchema):
    pass


class WorkspaceCreateSchema(WorkspaceCreateRequestSchema):
    user_id: int


class WorkspaceMemberCreateSchema(BaseModel):
    user_id: int
    workspace_id: int
    role: RoleLiteral | None = None


class AddMemberToWorkspaceSchema(BaseModel):
    user_id: int
    role: RoleLiteral | None = None


class WorkspaceReprSchema(WorkspaceBaseSchema):

    members: List[MemberCreateSchema]


class ChangeMemberRole(BaseModel):
    workspace_id: int
    member_id: int
    user_id: int
    role: RoleLiteral