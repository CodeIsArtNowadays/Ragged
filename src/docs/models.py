from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, func, Text
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from src.core.db import Base
from src.core.custom_types import StatusLiteral


class DocumentModel(Base):
    __tablename__ = 'documents'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(128))
    url: Mapped[str] = mapped_column(String(128))
    status: Mapped[StatusLiteral] = mapped_column(String(32), default='pending')
    is_active: Mapped[bool] = mapped_column(default=False)

    workspace_id: Mapped[int] = mapped_column(ForeignKey('workspaces.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('members.user_id'))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class ChunkModel(Base):
    __tablename__ = 'chunks'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str] = mapped_column(Text())
    document_index: Mapped[int] = mapped_column(index=True)
    embedding: Mapped[Vector] = mapped_column(Vector(384))
    
    document_id: Mapped[int] = mapped_column(ForeignKey('documents.id', ondelete='CASCADE'), index=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
