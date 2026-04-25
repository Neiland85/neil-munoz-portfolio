from uuid import UUID

from sqlmodel import Session, select

from app.models.project import Project


class ProjectService:
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

    def list_projects(self, session: Session) -> list[Project]:
        return list(session.exec(select(Project)).all())

    def get_project(self, session: Session, project_id: UUID) -> Project | None:
        return session.get(Project, project_id)

    def update_project(
        self,
        session: Session,
        project_id: UUID,
        name: str | None = None,
        description: str | None = None,
    ) -> Project | None:
        project = session.get(Project, project_id)

        if project is None:
            return None

        if name is not None:
            project.name = name

        if description is not None:
            project.description = description

        session.add(project)
        session.commit()
        session.refresh(project)
        return project

    def delete_project(self, session: Session, project_id: UUID) -> bool:
        project = session.get(Project, project_id)

        if project is None:
            return False

        session.delete(project)
        session.commit()
        return True
