from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_project():
    response = client.post(
        "/api/v1/projects", json={"name": "Test Project", "description": "Testing creation"}
    )
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Test Project"
    assert data["description"] == "Testing creation"
    assert "id" in data


def test_list_projects():
    response = client.get("/api/v1/projects")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)


def test_get_project_by_id():
    create_response = client.post(
        "/api/v1/projects", json={"name": "Project X", "description": "Lookup test"}
    )
    project = create_response.json()
    project_id = project["id"]

    response = client.get(f"/api/v1/projects/{project_id}")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == project_id


def test_get_project_not_found():
    fake_id = "00000000-0000-0000-0000-000000000000"

    response = client.get(f"/api/v1/projects/{fake_id}")
    assert response.status_code == 404


def test_update_project():
    create_response = client.post(
        "/api/v1/projects",
        json={"name": "Old name", "description": "Old description"},
    )
    project = create_response.json()
    project_id = project["id"]

    update_response = client.put(
        f"/api/v1/projects/{project_id}",
        json={"name": "New name", "description": "New description"},
    )
    assert update_response.status_code == 200

    data = update_response.json()
    assert data["id"] == project_id
    assert data["name"] == "New name"
    assert data["description"] == "New description"


def test_delete_project():
    create_response = client.post(
        "/api/v1/projects",
        json={"name": "Delete me", "description": "To be removed"},
    )
    project = create_response.json()
    project_id = project["id"]

    delete_response = client.delete(f"/api/v1/projects/{project_id}")
    assert delete_response.status_code == 204
    assert delete_response.text == ""

    get_response = client.get(f"/api/v1/projects/{project_id}")
    assert get_response.status_code == 404
