from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "").lower()


def test_healthcheck() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert "service" in data


def test_health_config_does_not_expose_secrets() -> None:
    response = client.get("/api/v1/system/config")
    assert response.status_code == 200

    data = response.json()
    assert "DATABASE_URL" not in data
    assert "SECRET_KEY" not in data
