from typing import List

from fastapi import APIRouter, Depends, Body

from src.workspaces.models import MemberModel
from src.workspaces.service import WorkspaceService
from src.workspaces.schemas import WorkspaceCreateRequestSchema, AddMemberToWorkspaceSchema, WorkspaceReprSchema, WorkspaceListSchema
from src.workspaces.dependencies import get_member, get_workspace_service, Permission


workspaces_router = APIRouter()

# PUBLIC

@workspaces_router.get('/index')
async def index():
    return {'me': 'KING'}

# AUTHENTICATED

@workspaces_router.get('/', response_model=List[WorkspaceListSchema])
async def get_workspaces(
    user: MemberModel = Depends(get_member),
    workspace_service: WorkspaceService = Depends(get_workspace_service)
):
    return await workspace_service.get_users_workspaces(user.user_id)

@workspaces_router.post('/')
async def create_workspace(
    workspace_data: WorkspaceCreateRequestSchema,
    workspace_service: WorkspaceService = Depends(get_workspace_service),
    member: MemberModel = Depends(get_member)
):
    return await workspace_service.create_workspace(workspace_data, member.user_id)

# AUTHORIZED

@workspaces_router.get('/{id}', response_model=WorkspaceReprSchema)
async def get_workspace(
    workspace_id: int, 
    user: MemberModel = Depends(Permission(['owner', 'admin', 'member'])),
    workspace_service: WorkspaceService = Depends(get_workspace_service)
):
    return await workspace_service.get_workspace(workspace_id, user.user_id)

@workspaces_router.patch('/{id}')
async def add_member_to_workspace(
    workspace_id: int,
    member_to_add: AddMemberToWorkspaceSchema,
    user: MemberModel = Depends(Permission(['owner'])),
    workspace_service: WorkspaceService = Depends(get_workspace_service)
):
    return await workspace_service.add_member_to_workspace(workspace_id, user, member_to_add)

@workspaces_router.delete('/{id}/members')
async def kick_member(
    workspace_id: int, 
    member_to_kick_id: int = Body(embed=True), 
    user: MemberModel = Depends(Permission(['owner'])), 
    workspace_service: WorkspaceService = Depends(get_workspace_service)
):
    if await workspace_service.kick_member(workspace_id, user.user_id, member_to_kick_id):
        return {'status': 204}
    raise Exception # todo refactor to get_member_by_id
    
