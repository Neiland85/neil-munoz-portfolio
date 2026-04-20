from uuid import UUID

from sqlmodel import Session, select

from app.models.project import Project


class ProjectService:
    def list_projects(self, session: Session) -> list[Project]:
        statement = select(Project).order_by(Project.created_at.desc())
        return list(session.exec(statement).all())

    def create_project(
        self,
        session: Session,
        name: str,
        description: str | None = None,
    ) -> Project:
        project = Project(name=name, description=description)
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    def get_project(self, session: Session, project_id: UUID) -> Project | None:
        return session.get(Project, str(project_id))

    def update_project(
        self,
        session: Session,
        project_id: UUID,
        name: str,
        description: str | None = None,
    ) -> Project | None:
        project = session.get(Project, str(project_id))
        if project is None:
            return None

        project.name = name
        project.description = description
        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    def delete_project(self, session: Session, project_id: UUID) -> bool:
        project = session.get(Project, str(project_id))
        if project is None:
            return False

        session.delete(project)
        session.commit()
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
