from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/system", tags=["system"])


@router.get("/config")
def system_config() -> dict[str, str]:
    return {
        "service": "portfolio-api",
        "environment": "test",
    }
