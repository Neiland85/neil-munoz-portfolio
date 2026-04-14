from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/config", summary="Non-sensitive configuration summary")
def health_config() -> dict[str, object]:
    settings = get_settings()
    return settings.safe_summary()
