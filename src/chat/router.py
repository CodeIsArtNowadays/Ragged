from fastapi import APIRouter, WebSocket, Depends
from fastapi.websockets import WebSocketDisconnect

from src.chat.service import websocket_manager
from src.chat.utils import verify_membership, get_member_by_token
from src.auth.service import UserService
from src.auth.dependencies import get_user_service
from src.workspaces.models import MemberModel
from src.workspaces.service import WorkspaceService
from src.workspaces.repository import MemberRepository
from src.workspaces.dependencies import Permission, get_member_repo, get_workspace_service


chat_router = APIRouter(prefix='/{workspace_id}')


@chat_router.get('/channel')
async def channel(workspace_id: int, user: MemberModel = Depends(Permission(['owner', 'admin', 'member']))):
    pass # message history with cursor based pagination


@chat_router.get('/test/{w_id}/{u_id}')
async def test(w_id: int, u_id: int,  workspace_service: WorkspaceService = Depends(get_workspace_service)):
    return await verify_membership(w_id, u_id, workspace_service)


@chat_router.websocket('/channel')
async def ws_handler(
    workspace_id: int, 
    websocket: WebSocket,
    user_service: UserService = Depends(get_user_service),
    member_repo: MemberRepository = Depends(get_member_repo),
    workspace_service: WorkspaceService = Depends(get_workspace_service)
    
): # accept - validate {'type': 'auth', 'data': token} - conman.connect - while True
    await websocket.accept() 
    try:
        
        data = await websocket.receive_json()
        if data['type'] == 'auth':
            member = await get_member_by_token(data['content']['token'], user_service, member_repo)
            if await verify_membership(workspace_id, member.user_id, workspace_service):
                await websocket_manager.connect(workspace_id, websocket)
                while True: 
                    data = await websocket.receive_json()
                    if data['type'] == 'message':
                        await websocket_manager.broadcast(workspace_id, data['content']['message'])
        else:
            await websocket.close(1008)
    except WebSocketDisconnect:
        await websocket_manager.disconnect(workspace_id, websocket)

    
