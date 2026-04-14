from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Project:
    id: UUID
    name: str
    description: str | None = None

    @staticmethod
    def create(name: str, description: str | None = None) -> "Project":
        return Project(
            id=uuid4(),
            name=name,
            description=description,
        )
