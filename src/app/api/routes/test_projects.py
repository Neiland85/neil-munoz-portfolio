import datetime
import uuid
from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.routes.projects import router
from app.core.db import get_session

# Creamos una app FastAPI temporal e incluimos el router a probar
app = FastAPI()
app.include_router(router)

# Anulamos la dependencia de la base de datos para no requerir conexión real
app.dependency_overrides[get_session] = lambda: MagicMock()

client = TestClient(app)


@pytest.fixture
def mock_project_service():
    # Interceptamos el ProjectService instanciado a nivel de módulo
    with patch("app.api.routes.projects.project_service") as mock_service:
        yield mock_service


@pytest.fixture
def project_id():
    return uuid.uuid4()


@pytest.fixture
def sample_project(project_id):
    # Creamos un objeto simulado que represente una entidad de la base de datos
    mock_project = MagicMock()
    mock_project.id = project_id
    mock_project.name = "Test Project"
    mock_project.description = "Test Description"
    mock_project.created_at = datetime.datetime.now(datetime.timezone.utc)
    mock_project.updated_at = datetime.datetime.now(datetime.timezone.utc)
    return mock_project


def test_create_project(mock_project_service, sample_project):
    mock_project_service.create_project.return_value = sample_project

    response = client.post(
        "/api/v1/projects", json={"name": "Test Project", "description": "Test Description"}
    )

    assert response.status_code == 201
    assert response.json()["id"] == str(sample_project.id)
    assert response.json()["name"] == "Test Project"


def test_list_projects(mock_project_service, sample_project):
    mock_project_service.list_projects.return_value = [sample_project]

    response = client.get("/api/v1/projects")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == str(sample_project.id)


def test_get_project_success(mock_project_service, sample_project, project_id):
    mock_project_service.get_project.return_value = sample_project

    response = client.get(f"/api/v1/projects/{project_id}")

    assert response.status_code == 200
    assert response.json()["id"] == str(project_id)


def test_get_project_not_found(mock_project_service, project_id):
    mock_project_service.get_project.return_value = None

    response = client.get(f"/api/v1/projects/{project_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Project not found"


def test_update_project_success(mock_project_service, sample_project, project_id):
    mock_project_service.update_project.return_value = sample_project

    response = client.put(
        f"/api/v1/projects/{project_id}",
        json={"name": "Updated Name", "description": "Updated Description"},
    )

    assert response.status_code == 200
    assert response.json()["id"] == str(project_id)


def test_delete_project_success(mock_project_service, project_id):
    mock_project_service.delete_project.return_value = True

    response = client.delete(f"/api/v1/projects/{project_id}")

    assert response.status_code == 204
