from datetime import datetime
from uuid import uuid4

from sqlmodel import Field, SQLModel


class Project(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    name: str
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
