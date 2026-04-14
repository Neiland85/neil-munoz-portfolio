import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_v1_router
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.core.middleware import request_logging_middleware

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    setup_logging(settings.LOG_LEVEL)

    logger.info("Starting application...")
    logger.info("Environment: %s", settings.APP_ENV)
    logger.info("Debug mode: %s", settings.APP_DEBUG)

    if settings.is_production and settings.APP_DEBUG:
        raise RuntimeError("APP_DEBUG must be False in production")

    if settings.is_production and not settings.SECRET_KEY:
        raise RuntimeError("SECRET_KEY must be set in production")

    app.state.settings = settings

    logger.info("Application startup complete")

    yield

    logger.info("Shutting down application")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.APP_DEBUG,
        lifespan=lifespan,
    )

    app.middleware("http")(request_logging_middleware)

    @app.get("/", tags=["root"], summary="Service metadata")
    def root() -> dict[str, str]:
        return {
            "service": settings.APP_NAME,
            "environment": settings.APP_ENV,
            "docs": "/docs",
            "openapi": "/openapi.json",
            "api_v1": "/api/v1",
        }

    app.include_router(api_v1_router)

    return app


app = create_app()
