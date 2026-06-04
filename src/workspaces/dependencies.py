from loguru import logger
from workspaces.models import MemberModel
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_db
from src.core.dependencies import get_user
from src.core.custom_types import RoleLiteral
from src.auth.models import UserModel
from src.workspaces.service import WorkspaceService
from src.workspaces.repository import MemberRepository, WorkspaceRepository, WorkspaceMemberRepository


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

    async def __call__(self, 
        id: int, 
        role: RoleLiteral,
        wm_repo: WorkspaceMemberRepository = Depends(get_workspace_member_repo),
        member: MemberModel = Depends(get_member)
    ):
        member_role = await wm_repo.member_role(id, member.user_id)
        if not member_role == role:
            logger.error('Permission Denied')
            raise Exception
        return member
        