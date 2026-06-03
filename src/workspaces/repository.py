from sqlalchemy.orm import selectinload
from sqlalchemy import select

from src.core.generic_repository import BaseRepository
from src.workspaces.models import MemberModel
from src.workspaces.models import WorkspaceModel, WorkspaceMember


class MemberRepository(BaseRepository):
    model = MemberModel

    async def get_member_by_user_id(self, user_id) -> MemberModel | None:
        stmt = select(MemberModel).where(user_id == user_id)
        return await self.session.scalar(stmt)


class WorkspaceRepository(BaseRepository):
    model = WorkspaceModel


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