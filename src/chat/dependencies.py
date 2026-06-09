from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_db
from src.chat.repository import MessageRepository


class PaginationParams():

    def __init__(self, size=200, cursor=None):
        self.size = size
        self.cursor = cursor


def get_message_repo(session: AsyncSession = Depends(get_db)):
    return MessageRepository(session)

# def get_channel_repo(session: AsyncSession = Depends(get_db)):
#     return ChannelRepository(session)