from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine

from app.core.config import get_settings

settings = get_settings()

if settings.APP_ENV == "prod":
    database_url = settings.DATABASE_URL  # validated in Settings
else:
    database_url = settings.DATABASE_URL or "sqlite:///./data/local.db"

connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}

engine: Engine = create_engine(database_url, echo=False, connect_args=connect_args)


def init_db() -> None:
    import app.models.project  # noqa: F401

    SQLModel.metadata.create_all(engine)
