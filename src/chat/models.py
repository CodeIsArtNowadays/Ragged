from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import Base


# class ChannelModel(Base):
#     __tablename__ = 'channels'

#     id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     workspace_id: Mapped[int] = mapped_column(ForeignKey('workspaces.id', ondelete='CASCADE'), index=True, unique=True)

#     # workspace: Mapped['WorkspaceModel'] = relationship('WorkspaceModel', back_populates='channel') # noqa: F821  
#     messages: Mapped[List[MessageModel]] = relationship('MessageModel', back_populates='channel')

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now()
#     )
#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
#     )


class MessageModel(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text())
    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspaces.id', ondelete='CASCADE'), index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('members.user_id'), index=True)

    # channel: Mapped['ChannelModel'] = relationship(ChannelModel, back_populates='messages')
    # # author: Mapped['MemberModel'] = relationship('MemberModel', back_populates='messages') # noqa: F821  

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(),
        index=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )