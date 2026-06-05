from src.core.generic_repository import BaseRepository

from src.chat.models import ChannelModel, MessageModel


class ChannelRepository(BaseRepository):
    
    model = ChannelModel

    async def get_or_create(self, workspace_id: int):
        pass


class MessageRepository(BaseRepository):
    model = MessageModel

