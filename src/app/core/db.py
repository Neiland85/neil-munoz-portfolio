from sqlalchemy import Engine
from sqlmodel import create_engine

from app.core.config import get_settings

settings = get_settings()

if settings.APP_ENV == "prod":
    database_url = settings.DATABASE_URL  # validado en config
else:
    database_url = settings.DATABASE_URL or "sqlite:///./data/local.db"

engine: Engine = create_engine(database_url, echo=False)
