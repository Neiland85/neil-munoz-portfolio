from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session

from app.core.deps import get_session
<<<<<<< Updated upstream
=======
from app.models import project
>>>>>>> Stashed changes
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.services import project_service
from app.services.project_service import ProjectService


router = APIRouter(prefix="/api/v1/projects", tags=["projects"])

DB: dict[str, dict[str, Any]] = {}  # noqa: F821


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    session: Session = Depends(get_session),
) -> ProjectResponse:
<<<<<<< Updated upstream
    project = project_service.create_project(
=======
    project = project_service.create_project(  # pyright: ignore[reportAttributeAccessIssue]
>>>>>>> Stashed changes
        session=session,
        name=payload.name,
        description=payload.description,
    )
    return ProjectResponse.model_validate(project)


<<<<<<< Updated upstream
@router.get("", response_model=list[ProjectResponse])
def list_projects(session: Session = Depends(get_session)) -> list[ProjectResponse]:
    projects = project_service.list_projects(session=session)
    return [ProjectResponse.model_validate(project) for project in projects]


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: UUID,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.get_project(session=session, project_id=project_id)
=======
@router.get("")
def list_projects() -> list[dict[str, Any]]:
    return list(DB.values())


@router.get("/{project_id}")
def get_project(project_id: UUID) -> dict[str, Any]:
    key = str(project_id)
    project = DB.get(key)
>>>>>>> Stashed changes

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse.model_validate(project)  # type: ignore


<<<<<<< Updated upstream
@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: UUID,
    payload: ProjectUpdate,
    session: Session = Depends(get_session),
) -> ProjectResponse:
    project = project_service.update_project(
        session=session,
        project_id=project_id,
        name=payload.name,
        description=payload.description,
    )
=======
@router.put("/{project_id}")
def update_project(project_id: UUID, payload: dict[str, Any]) -> dict[str, Any]:
    key = str(project_id)
>>>>>>> Stashed changes

    if key not in DB:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse.model_validate(project)  # type: ignore # noqa: F821


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
<<<<<<< Updated upstream
def delete_project(
    project_id: UUID,
    session: Session = Depends(get_session),
) -> Response:
    deleted = project_service.delete_project(session=session, project_id=project_id)
=======
def delete_project(project_id: UUID) -> Response:
    key = str(project_id)
>>>>>>> Stashed changes

    if key not in DB:
        raise HTTPException(status_code=404, detail="Project not found")

    del DB[key]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
