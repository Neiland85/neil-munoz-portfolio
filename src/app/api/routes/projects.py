from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from fastapi import APIRouter, HTTPException, Response, status

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])

DB: dict[str, dict[str, Any]] = {}


@router.post("", status_code=status.HTTP_201_CREATED)
def create_project(payload: dict[str, Any]) -> dict[str, Any]:
    project_id = str(uuid4())

    project = {
        "id": project_id,
        "name": payload.get("name"),
        "description": payload.get("description"),
    }

    DB[project_id] = project
    return project


@router.get("")
def list_projects() -> list[dict[str, Any]]:
    return list(DB.values())


@router.get("/{project_id}")
def get_project(project_id: UUID) -> dict[str, Any]:
    key = str(project_id)
    project = DB.get(key)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.put("/{project_id}")
def update_project(project_id: UUID, payload: dict[str, Any]) -> dict[str, Any]:
    key = str(project_id)

    if key not in DB:
        raise HTTPException(status_code=404, detail="Project not found")

    DB[key].update(payload)
    return DB[key]


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: UUID) -> Response:
    key = str(project_id)

    if key not in DB:
        raise HTTPException(status_code=404, detail="Project not found")

    del DB[key]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
