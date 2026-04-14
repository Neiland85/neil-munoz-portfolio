from sqlmodel import create_engine

from app.core.config import get_settings

settings = get_settings()

database_url = settings.DATABASE_URL or "sqlite:///./data/local.db"
engine = create_engine(database_url, echo=False)
