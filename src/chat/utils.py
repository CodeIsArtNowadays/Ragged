from src.workspaces.models import MemberModel
from src.auth.service import UserService
from src.workspaces.repository import MemberRepository
from src.workspaces.service import WorkspaceService


async def get_member_by_token(
    token: str,
    user_service: UserService,
    member_repo: MemberRepository
) -> MemberModel:
    user_payload = await user_service.decode_jwt_token(token)

    member = await member_repo.get_member_by_user_id(user_payload['user_id'])
    if not member: 
        raise Exception # TODO: faKing exc

    return member


async def verify_membership(
    workspace_id: int, 
    user_id: int,
    workspace_service: WorkspaceService
):
    role = await workspace_service.get_member_role(workspace_id, user_id)
    return bool(role)
    