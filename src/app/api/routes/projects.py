from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session, select

from app.core.deps import get_session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectResponse

router = APIRouter(prefix="/projects", tags=["projects"])

SessionDep = Annotated[Session, Depends(get_session)]


@router.get("", response_model=list[ProjectResponse])
def list_projects(session: SessionDep):
    statement = select(Project)
    results = session.exec(statement)
    return results.all()


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate, session: SessionDep):
    db_project = Project.model_validate(project)
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: UUID, session: SessionDep):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: UUID, project_in: ProjectCreate, session: SessionDep):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.name = project_in.name
    project.description = project_in.description

    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: UUID, session: SessionDep):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    session.delete(project)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
