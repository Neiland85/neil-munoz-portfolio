from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.projects import router as projects_router
from app.api.routes.system import router as system_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(health_router)
api_v1_router.include_router(system_router)
api_v1_router.include_router(projects_router)
