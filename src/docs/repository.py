from src.core.generic_repository import BaseRepository
from src.core.custom_types import StatusLiteral
from src.docs.models import DocumentModel, ChunkModel


class DocumentRepository(BaseRepository):
    model = DocumentModel

    async def set_status(self, document_id: int, status=StatusLiteral):
        document = await self.get_by_id(document_id)
        if not document:
            raise Exception # TODO: exc

        document.status = status
        await self.session.flush()

class ChunkRepository(BaseRepository):
    model = ChunkModel
        