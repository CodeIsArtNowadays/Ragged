from fastapi import APIRouter, Depends

from src.workspaces.models import MemberModel
from src.workspaces.service import WorkspaceService
from src.workspaces.schemas import WorkspaceCreateRequestSchema, AddMemberToWorkspaceSchema, WorkspaceReprSchema
from src.workspaces.dependencies import get_member, get_workspace_service


workspaces_router = APIRouter()


@workspaces_router.get('/index')
async def index():
    return {'me': 'KING'}


@workspaces_router.post('/')
async def create_workspace(
    workspace_data: WorkspaceCreateRequestSchema,
    workspace_service: WorkspaceService = Depends(get_workspace_service),
    member: MemberModel = Depends(get_member)
):
    return await workspace_service.create_workspace(workspace_data, member.user_id)


@workspaces_router.patch('/{id}')
async def add_member_to_workspace(
    id: int,
    member_to_add: AddMemberToWorkspaceSchema,
    user: MemberModel = Depends(get_member),
    workspace_service: WorkspaceService = Depends(get_workspace_service)
):
    return await workspace_service.add_member_to_workspace(id, user, member_to_add)


@workspaces_router.get('/{id}', response_model=WorkspaceReprSchema)
async def get_workspace(id: int, user: MemberModel = Depends(get_member), workspace_service: WorkspaceService = Depends(get_workspace_service)):
    return await workspace_service.get_workspace(id, user.user_id) 
    