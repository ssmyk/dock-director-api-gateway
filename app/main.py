from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import container_manager
from app.settings import settings

app = FastAPI(title="DockDirector API Gateway", debug=settings.DEBUG)

origins = []
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)

app.include_router(container_manager.router)
