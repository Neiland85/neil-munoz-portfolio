from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes.health import router as health_router  # noqa: E402
from app.api.routes.projects import router as projects_router  # noqa: E402
from app.api.routes.system import router as system_router  # noqa: E402
from app.api.routes.web import router as web_router  # noqa: E402
from app.core.config import get_settings  # noqa: E402
from app.core.db import init_db  # noqa: E402
from app.core.logging import setup_logging  # noqa: E402
from app.core.middleware import ConsentCookieMiddleware, SecurityHeadersMiddleware  # noqa: E402
from app.api.routes.health import router as health_router
from app.api.routes.projects import router as projects_router
from app.api.routes.system import router as system_router
from app.api.routes.web import router as web_router
from app.core.config import get_settings
from app.core.db import init_db
from app.core.logging import setup_logging
from app.core.middleware import ConsentCookieMiddleware, SecurityHeadersMiddleware

settings = get_settings()


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    setup_logging(settings.LOG_LEVEL)
    init_db()
    yield


app = FastAPI(lifespan=lifespan)
settings = get_settings()

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/app/static"), name="static")

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
