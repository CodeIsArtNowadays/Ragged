from loguru import logger
from sqlalchemy.orm import selectinload
from sqlalchemy import select, delete

from src.core.generic_repository import BaseRepository
from src.core.custom_types import RoleLiteral
from src.workspaces.models import MemberModel
from src.workspaces.models import WorkspaceModel, WorkspaceMember


class MemberRepository(BaseRepository):
    model = MemberModel

    async def get_member_by_user_id(self, user_id) -> MemberModel | None:
        stmt = select(MemberModel).where(user_id == user_id)
        return await self.session.scalar(stmt)


class WorkspaceRepository(BaseRepository):
    model = WorkspaceModel

    async def get_user_workspaces(self, user_id: int):
        stmt = select(WorkspaceModel).join(WorkspaceMember, WorkspaceModel.id == WorkspaceMember.workspace_id).where(WorkspaceMember.user_id == user_id)
        res = await self.session.scalars(stmt)
        return res.all()

class WorkspaceMemberRepository(BaseRepository):
    model = WorkspaceMember

    async def member_role(self, workspace_id: int, user_id: int):
        stmt = select(WorkspaceMember.role).where(WorkspaceMember.workspace_id == workspace_id, WorkspaceMember.user_id == user_id)
        return await self.session.scalar(stmt)

    async def get_workspace_members(self, workspace_id: int):
        stmt = select(WorkspaceMember).where(
            WorkspaceMember.workspace_id == workspace_id
        ).options(selectinload(WorkspaceMember.user))
        res = await self.session.scalars(stmt)
        return res.all()

    async def delete_by_user_id(self, workspace_id: int, member_id: int):
        stmt = delete(WorkspaceMember).where(WorkspaceMember.workspace_id == workspace_id, WorkspaceMember.user_id == member_id)
        await self.session.execute(stmt)

    async def change_member_role(self, workspace_id: int, member_id: int, role: RoleLiteral):
        stmt = select(WorkspaceMember).where(WorkspaceMember.workspace_id == workspace_id, WorkspaceMember.user_id == member_id)
        res = await self.session.execute(stmt)
        mu = res.scalar_one()
        if not mu:
            logger.error('No member')
        mu.role = role
        await self.session.flush()
        await self.session.refresh(mu)
        return mu

    
        