from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.projects import router as projects_router
from app.api.routes.system import router as system_router
from app.api.routes.web import router as web_router
from app.core.config import get_settings
from app.core.middleware import ConsentCookieMiddleware, SecurityHeadersMiddleware

settings = get_settings()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins
    or [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(ConsentCookieMiddleware)

app.include_router(web_router)
app.include_router(health_router)
app.include_router(system_router)
app.include_router(projects_router)


@app.get("/health")
def root_health() -> dict[str, str]:
    return {"status": "ok"}
