from uuid import UUID

from app.domain.project import Project


class ProjectService:
    def __init__(self) -> None:
        self._projects: dict[UUID, Project] = {}

    def list_projects(self) -> list[Project]:
        return list(self._projects.values())

    def create_project(self, name: str, description: str | None = None) -> Project:
        project = Project.create(name=name, description=description)
        self._projects[project.id] = project
        return project

    def get_project(self, project_id: UUID) -> Project | None:
        return self._projects.get(project_id)

    def update_project(
        self, project_id: UUID, name: str, description: str | None = None
    ) -> Project | None:
        project = self._projects.get(project_id)
        if project is None:
            return None

        project.name = name
        project.description = description
        return project

    def delete_project(self, project_id: UUID) -> bool:
        if project_id not in self._projects:
            return False

        del self._projects[project_id]
        return True
