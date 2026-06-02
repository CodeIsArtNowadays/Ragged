import jwt

from pwdlib import PasswordHash

from config import settings
from src.auth.repository import UserRepository
from src.auth.schemas import UserCredentialsSchema
from src.auth.exceptions import UserException


class UserService:

    def __init__(self, repo: UserRepository):
        self.repo = repo
        self.hashier = PasswordHash.recommended()

    async def create_user(self, data: UserCredentialsSchema):
        password = data.password
        hashed_password = await self.hash_password(password)
        data.password = hashed_password
        return self.repo.create(data)

    async def hash_password(self, pswd: str) -> str:
        return self.hashier.hash(pswd)

    async def login(self, data: UserCredentialsSchema):
        user = await self.repo.get_by_username(data.username)
        if not user:
            raise UserException

        if not await self.verify_password(data.password, user.password):
            raise UserException

        payload = {
            'user_id': user.id,
            'username': user.username
        }
        return await self.create_jwt_token(payload)

    async def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.hashier.verify(password, hashed_password)

    async def create_jwt_token(self, payload):
        return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')

    async def decode_jwt_token(self, token):
        return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])