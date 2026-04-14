from sqlmodel import create_engine

from app.core.config import Settings, get_settings

settings: Settings = get_settings()

database_url: str = settings.DATABASE_URL or "sqlite:////data/local.db"

engine = create_engine(database_url, echo=False)
