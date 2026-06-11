import aiofiles

from pathlib import Path

from src.docs.repository import DocumentRepository
from src.docs.schemas import DocumentCreateSchema


class DocumentService:

    def __init__(self, repo: DocumentRepository):
        self.repo = repo

    async def upload_file(self, workspace_id: int, author_id: int, file):
        file_path = await self.save_file(workspace_id, file)
        document_data = DocumentCreateSchema(
            title=file.filename,
            author_id=author_id,
            workspace_id=workspace_id,
            url=file_path
        )
        document = await self.repo.create(document_data)
        await self.repo.set_status(document.id, 'processing')
        return document

    async def save_file(self, workspace_id: int, file):
        upload_dir = Path(f'docs/{workspace_id}')
        upload_dir.mkdir(parents=True, exist_ok=True)
        file_path = upload_dir / file.filename

        async with aiofiles.open(file_path, 'wb') as f:
            while content := await file.read(1024 * 1024):
                await f.write(content)

        return str(file_path)

