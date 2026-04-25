from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import logger


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception(
        "unhandled_server_error",
        extra={
            "path": request.url.path,
            "method": request.method,
            "client_ip": request.client.host if request.client else None,
            "error": str(exc),
        },
    )

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )
