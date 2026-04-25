from collections.abc import Generator

from sqlalchemy.pool import StaticPool
from sqlmodel import SQLModel, Session, create_engine

from app.core.config import get_settings


def _build_engine():
    database_url = get_settings().DATABASE_URL or "sqlite:///./data/local.db"

    if database_url.startswith("sqlite"):
        return create_engine(
            database_url,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool if database_url in {"sqlite://", "sqlite:///:memory:"} else None,
        )

    return create_engine(database_url)


engine = _build_engine()


def init_db() -> None:
    from app.models import project  # noqa: F401

    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    init_db()
    with Session(engine) as session:
        yield session
