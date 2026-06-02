
from src.core.generic_repository import BaseRepository
from src.api.models import MemberModel


class MemberRepository(BaseRepository):
    model = MemberModel
