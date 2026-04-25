from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session

from app.core.db import get_session
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services.project_service import ProjectService

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])

project_service = ProjectService()
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services.project_service import ProjectService

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])

@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.create_project(
        session=session,
        name=payload.name,
        description=payload.description,
    )
    return ProjectResponse.model_validate(project)


@router.get("", response_model=list[ProjectResponse])
def list_projects(
    session: Session = Depends(get_session),
) -> list[ProjectResponse]:
    projects = project_service.list_projects(session=session)
    return [ProjectResponse.model_validate(project) for project in projects]


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: UUID,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.get_project(session=session, project_id=project_id)
project_service = ProjectService()


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.create_project(
        session=session,
        name=payload.name,
        description=payload.description,
    )
    return ProjectResponse.model_validate(project)


@router.get("", response_model=list[ProjectResponse])
def list_projects(
    session: Session = Depends(get_session),
) -> list[ProjectResponse]:
    projects = project_service.list_projects(session=session)
    return [ProjectResponse.model_validate(project) for project in projects]


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: UUID,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.get_project(
        session=session,
        project_id=project_id,
    )
    project = project_service.get_project(session=session, project_id=project_id)  # pyright: ignore[reportCallIssue]

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse.model_validate(project)


@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: UUID,
    payload: ProjectUpdate,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.update_project(
        session=session,
    project = project_service.update_project(
        session=session,
def update_project(project_id: UUID, payload: ProjectUpdate) -> ProjectResponse:
    project = project_service.update_project(
        session=session,  # type: ignore
        project_id=project_id,
        name=payload.name,
        description=payload.description,
    )

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse.model_validate(project)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: UUID,
    session: Session = Depends(get_session),
) -> Response:
    deleted = project_service.delete_project(
        session=session,
        project_id=project_id,
    )
        session=session,  # pyright: ignore[reportCallIssue]
        project_id=project_id,
    )
        session=session,
        project_id=project_id,
    )
def delete_project(project_id: UUID) -> Response:
    deleted = project_service.delete_project(project_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Project not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
