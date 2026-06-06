from workspaces.models import MemberModel
from fastapi import APIRouter, WebSocket, Depends

from src.chat.service import websocket_manager
from src.workspaces.dependencies import Permission


chat_router = APIRouter(prefix='/{workspace_id}')


@chat_router.get('/channel')
async def channel(workspace_id: int, user: MemberModel = Depends(Permission(['owner', 'admin', 'member']))):
    pass # message history with cursor based pagination


@chat_router.websocket('/channel')
async def ws_handler(workspace_id: int, websocket: WebSocket): # accept - validate {'type': 'auth', 'token': token} - conman.connect - while True
    await websocket_manager.connect(workspace_id, websocket) 
    while True: 
        data = await websocket.receive()
        await websocket_manager.broadcast(workspace_id, data['text'])


    
