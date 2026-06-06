from loguru import logger

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_db
from src.core.dependencies import get_user
from src.auth.models import UserModel
from src.workspaces.service import WorkspaceService
from src.workspaces.models import MemberModel
from src.workspaces.repository import MemberRepository, WorkspaceRepository, WorkspaceMemberRepository
from src.workspaces.exceptions import PermissionDeniedException


async def get_member_repo(session: AsyncSession = Depends(get_db)):
    return MemberRepository(session)

async def get_member(
    user: UserModel = Depends(get_user),
    member_repo: MemberRepository = Depends(get_member_repo)
):
    return await member_repo.get_member_by_user_id(user.id)

async def get_workspace_repo(session: AsyncSession = Depends(get_db)):
    return WorkspaceRepository(session)

async def get_workspace_member_repo(session: AsyncSession = Depends(get_db)):
    return WorkspaceMemberRepository(session)

async def get_workspace_service(
    workspace_repo: WorkspaceRepository = Depends(get_workspace_repo),
    ws_member_repo: WorkspaceMemberRepository = Depends(get_workspace_member_repo)
):
    return WorkspaceService(workspace_repo, ws_member_repo)


class Permission:

    def __init__(self, roles: list):
        self.roles = roles

    async def __call__(
        self, 
        workspace_id: int,
        wm_repo: WorkspaceMemberRepository = Depends(get_workspace_member_repo),
        member: MemberModel = Depends(get_member)
    ):
        member_role = await wm_repo.member_role(workspace_id, member.user_id)
        if member_role not in self.roles:
            logger.error('Permission Denied')
            raise PermissionDeniedException
        return member
        