from loguru import logger

from src.workspaces.models import MemberModel
from src.workspaces.schemas import WorkspaceCreateRequestSchema, WorkspaceMemberCreateSchema, AddMemberToWorkspaceSchema, WorkspaceReprSchema, MemberCreateSchema
from src.workspaces.repository import WorkspaceRepository, WorkspaceMemberRepository


class WorkspaceService:

    def __init__(
        self, 
        workspace_repo: WorkspaceRepository,
        workspace_member_repo: WorkspaceMemberRepository
    ):
        self.workspace_repo = workspace_repo
        self.workspace_member_repo = workspace_member_repo

    async def create_workspace(self, workspace_request_data: WorkspaceCreateRequestSchema, user_id: int):
        workspace = await self.workspace_repo.create(workspace_request_data)
        workspace_member_data = WorkspaceMemberCreateSchema(workspace_id=workspace.id, user_id=user_id, role='owner')
        await self.workspace_member_repo.create(workspace_member_data)
        return workspace

    async def get_member_role(self, workspace_id: int, member_id: int):
        logger.info(member_id)
        return await self.workspace_member_repo.member_role(workspace_id, member_id)

    async def add_member_to_workspace(
        self, 
        workspace_id,
        member_from_request: MemberModel,
        member_data: AddMemberToWorkspaceSchema
    ):
        role = await self.get_member_role(workspace_id, member_from_request.user_id)
        if role != 'owner':
             logger.error('Owner only')
             raise Exception 

        member_workspace_data = WorkspaceMemberCreateSchema(
            workspace_id=workspace_id, 
            user_id=member_data.user_id,
            role=member_data.role
        )
        return await self.workspace_member_repo.create(member_workspace_data)

    async def get_workspace(self, workspace_id: int, user_id: int):
        role = await self.get_member_role(workspace_id, user_id)
        if not role:
            logger.error('Members only')
            raise Exception

        workspace = await self.workspace_repo.get_by_id(workspace_id) # title
        members = await self.workspace_member_repo.get_workspace_members(workspace_id) # usernames (id) + docs
        workspace_repr_data = WorkspaceReprSchema(
            title=workspace.title,
            members=[MemberCreateSchema(username=member.user.username, user_id=member.user_id) for member in members]
        )
        return workspace_repr_data