import asyncio
import aiofiles

from fastapi import Depends
from pypdf import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer

from src.docs.models import DocumentModel
from src.docs.repository import ChunkRepository
from src.docs.schemas import ChunkCreateSchema
from src.docs.dependencies import get_chunk_repo


semantic_model = SentenceTransformer("all-MiniLM-L6-v2")


class ProcessFile:

    def __init__(self, chunk_repo: ChunkRepository = Depends(get_chunk_repo)):
        self.chunk_repo = chunk_repo
        self.PARSERS = {
            'pdf': self.get_text_from_pdf,
            'txt': self.get_text_from_txt,
            'docx': self.get_text_from_docx
        }
        

    async def __call__(self, document: DocumentModel):
        document_extension = document.title.split('.')[-1]
        parser = self.PARSERS.get(document_extension)
        if not parser:
            raise Exception # TODO: exc

        text = await parser(document.url)
        chunks = await self.chunking_text(text) # chunks = [{'chunk_id': 1, 'text': text, 'embedding': [vec]}]
        for chunk in chunks:
            chunk['embedding'] = await self.embedding(chunk['text'])
            chunk_data = ChunkCreateSchema(
                document_id=document.id,
                document_index=chunk['chunk_id'],
                text=chunk['text'],
                embedding=chunk['embedding']
            )
            await self.chunk_repo.create(chunk_data)

    async def embedding(self, chunk):
        return await asyncio.to_thread(semantic_model.encode, chunk)

    async def chunking_text(self, text: str, size=300, overlap=50):
        res = []
        step = size - overlap
        for index, start in enumerate(range(0, len(text), step)):
            res.append({'chunk_id': index, 'text': text[start:start+size]})
        return res
        
    async def get_text_from_pdf(self, file_path: str):
        reader = PdfReader(file_path)
        text = '\n'.join(page.extract_text() for page in reader.pages)
        return text
        
    async def get_text_from_txt(self, file_path):
        async with aiofiles.open(file_path, 'r') as f:
            return await f.read()
            
    async def get_text_from_docx(self, file_path: str):
        file = Document(file_path)
        full_text = []

        for para in file.paragraphs:
            full_text.append(para.text)

        return '\n'.join(full_text)
