from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert "service" in data
    assert "environment" in data
    assert data["api_v1"] == "/api/v1"


def test_healthcheck() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert "service" in data
    assert "environment" in data


def test_health_config_does_not_expose_secrets() -> None:
    response = client.get("/api/v1/system/config")
    assert response.status_code == 200

    data = response.json()
    assert "SECRET_KEY" not in data
    assert "SMTP_PASSWORD" not in data
    assert "database_configured" in data
