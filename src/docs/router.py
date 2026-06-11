from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, BackgroundTasks

from src.docs.dependencies import get_docs_service
from src.docs.service import DocumentService
from src.docs.process_file import ProcessFile
from src.workspaces.models import MemberModel
from src.workspaces.dependencies import Permission


docs_router = APIRouter(prefix='/{workspace_id}')


@docs_router.post('/upload')
async def upload_document(
    workspace_id: int, 
    backgroud_task: BackgroundTasks,
    file: UploadFile = File(...),
    member: MemberModel = Depends(Permission(['owner', 'admin', 'member'])),
    docs_service: DocumentService = Depends(get_docs_service),
    process: ProcessFile = Depends(ProcessFile),
):
    allowed_extensions = {'pdf', 'docx', 'txt'}
    
    file_extension = file.filename.split('.')[-1].lower() if file.filename else ''

    if file_extension not in allowed_extensions:
        raise Exception # TODO: exc

    # TODO: exc
    try:
        document = await docs_service.upload_file(workspace_id, member.user_id, file)
    except Exception:
        raise HTTPException(status_code=404, detail='File upload error')

    backgroud_task.add_task(process, document)