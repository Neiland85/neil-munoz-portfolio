from sqlalchemy import Engine
from sqlmodel import create_engine

from app.core.config import Settings, get_settings

settings: Settings = get_settings()
database_url: str = settings.DATABASE_URL or "sqlite:///./data/local.db"


if settings.APP_ENV == "prod":
    database_url: str = settings.DATABASE_URL  # validated in Settings
else:
    database_url = settings.DATABASE_URL or "sqlite:///./data/local.db"
database_url: str = settings.DATABASE_URL or "sqlite:///./data/local.db"

engine: Engine = create_engine(database_url, echo=False)
database_url = settings.DATABASE_URL or "sqlite:///./data/local.db"

engine: Engine = create_engine(database_url, echo=False)
