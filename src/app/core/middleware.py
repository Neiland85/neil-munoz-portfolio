import logging
import time
from collections.abc import Awaitable, Callable

from fastapi import Request, Response

logger = logging.getLogger("app.request")


async def request_logging_middleware(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    start = time.perf_counter()
    response: Response | None = None

    try:
        response = await call_next(request)
        return response
    finally:
        duration_ms = round((time.perf_counter() - start) * 1000, 2)
        status_code = response.status_code if response is not None else 500

        logger.info(
            "method=%s path=%s status=%s duration_ms=%.2f",
            request.method,
            request.url.path,
            status_code,
            duration_ms,
        )
