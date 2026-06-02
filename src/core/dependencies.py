from loguru import logger

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.core.exceptions import AuthRequireException
from src.auth.service import UserService
from src.auth.models import UserModel
from src.auth.dependencies import get_user_service


bearer = HTTPBearer()


async def get_user(
    user_service: UserService = Depends(get_user_service),
    creds: HTTPAuthorizationCredentials | None = Depends(bearer)
) -> UserModel:

    if not creds:
        logger.error('Core|Dependencies|No creds')
        raise AuthRequireException

    token = creds.credentials
    decoded = await user_service.decode_jwt_token(token)

    if not decoded:
        logger.error('Core|Dependencies|No decoded')
        raise AuthRequireException

    user_id = int(decoded['user_id'])
    return await user_service.get_by_id(user_id)