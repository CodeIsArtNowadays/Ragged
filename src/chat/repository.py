from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload

from src.core.generic_repository import BaseRepository
from src.chat.models import MessageModel


# class ChannelRepository(BaseRepository):
    
#     model = ChannelModel

#     async def create_channel(self, workspace_id: int):
#         channel = ChannelModel(workspace_id=workspace_id)
#         self.session.add(channel)
#         await self.session.flush()
#         await self.session.refresh(channel)
#         return channel

#     async def get_or_create(self, workspace_id: int) -> ChannelModel:
#         stmt = select(ChannelModel).where(ChannelModel.workspace_id == workspace_id)
#         res = await self.session.scalar(stmt)

#         if not res:
#             return await self.create_channel(workspace_id)
#         return res


class MessageRepository(BaseRepository):
    model = MessageModel

    async def create(self, data):
        message = await super().create(data)
        stmt = select(MessageModel).where(MessageModel.id == message.id).options(selectinload(MessageModel.author))
        return await self.session.scalar(stmt)

    async def get_messages_by_workspace_id(self, workspace_id: int, size: int, cursor: int | None):
        stmt = select(MessageModel).where(MessageModel.workspace_id == workspace_id)
        if cursor:
            stmt = stmt.where(MessageModel.id < cursor)
        stmt = stmt.order_by(desc(MessageModel.id)).limit(size)

        res = await self.session.execute(stmt)
        return res.scalars().all()