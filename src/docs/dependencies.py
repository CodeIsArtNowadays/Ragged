from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_db
from src.docs.repository import DocumentRepository, ChunkRepository
from src.docs.service import DocumentService


def get_docs_repo(session: AsyncSession = Depends(get_db)):
    return DocumentRepository(session)

def get_docs_service(repo: DocumentRepository = Depends(get_docs_repo)):
    return DocumentService(repo)

def get_chunk_repo(session: AsyncSession = Depends(get_db)):
    return ChunkRepository(session)
