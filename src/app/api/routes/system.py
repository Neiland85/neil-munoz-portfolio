from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(prefix="/api/v1/system", tags=["system"])


@router.get("/config")
def system_config() -> dict[str, object]:
    settings = get_settings()
    return settings.safe_summary()
