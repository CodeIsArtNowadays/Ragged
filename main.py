from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.core.exceptions import ProjectBaseException
from src.auth.router import auth_router
from src.workspaces.router import workspaces_router
from src.chat.router import chat_router

app = FastAPI()

app.include_router(workspaces_router, prefix='')
app.include_router(auth_router, prefix='/auth')
app.include_router(chat_router)

@app.exception_handler(ProjectBaseException)
async def base_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})