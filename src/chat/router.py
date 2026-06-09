from fastapi import APIRouter, Depends, WebSocket
from fastapi.websockets import WebSocketDisconnect

from src.auth.dependencies import get_user_service
from src.auth.service import UserService
from src.chat.dependencies import PaginationParams, get_channel_repo, get_message_repo
from src.chat.repository import ChannelRepository, MessageRepository
from src.chat.schemas import MessageSchema
from src.chat.service import websocket_manager
from src.chat.utils import get_member_by_token, verify_membership
from src.workspaces.dependencies import (
    Permission,
    get_member_repo,
    get_workspace_service,
)
from src.workspaces.models import MemberModel
from src.workspaces.repository import MemberRepository
from src.workspaces.service import WorkspaceService

chat_router = APIRouter(prefix="/{workspace_id}")


@chat_router.get("/channel")
async def channel(
    workspace_id: int,
    user: MemberModel = Depends(Permission(["owner", "admin", "member"])),
    pagination: PaginationParams = Depends(),
    channel_repo: ChannelRepository = Depends(get_channel_repo),
    message_repo: MessageRepository = Depends(get_message_repo),
):
    channel = await channel_repo.get_or_create(workspace_id)
    return await message_repo.get_messages_by_channel_id(
        channel.id, pagination.size, pagination.cursor
    )

@chat_router.websocket("/channel")
async def ws_handler(
    workspace_id: int,
    websocket: WebSocket,
    user_service: UserService = Depends(get_user_service),
    member_repo: MemberRepository = Depends(get_member_repo),
    workspace_service: WorkspaceService = Depends(get_workspace_service),
    channel_repo: ChannelRepository = Depends(get_channel_repo),
    message_repo: MessageRepository = Depends(get_message_repo),
):
    await websocket.accept()
    try:
        data = await websocket.receive_json()
        if data["type"] == "auth":
            member = await get_member_by_token(
                data["content"]["token"], user_service, member_repo
            )
            channel = await channel_repo.get_or_create(workspace_id)
            if await verify_membership(workspace_id, member.user_id, workspace_service):
                await websocket_manager.connect(workspace_id, websocket)
                while True:
                    data = await websocket.receive_json()
                    if data["type"] == "message":
                        message_raw = data["content"]["message"]
                        message = MessageSchema(
                            text=message_raw,
                            author_id=member.user_id,
                            channel_id=channel.id,
                        )
                        message = await message_repo.create(message)
                        await websocket_manager.broadcast(
                            workspace_id, message.text
                        )  # TODO: broadcast json > text
        else:
            await websocket.close(1008)
    except WebSocketDisconnect:
        await websocket_manager.disconnect(workspace_id, websocket)
