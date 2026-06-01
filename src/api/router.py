from fastapi import APIRouter


api_router = APIRouter()


@api_router.get('/index')
async def index():
    return {'me': 'KING'}