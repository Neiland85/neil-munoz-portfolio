from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_healthcheck_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_returns_success() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "").lower()


def test_security_headers_present() -> None:
    response = client.get("/")
    assert response.headers.get("x-content-type-options") == "nosniff"
    assert response.headers.get("x-frame-options") == "DENY"
    assert response.headers.get("referrer-policy") == "strict-origin-when-cross-origin"
    assert "content-security-policy" in response.headers


def test_cookie_consent_is_set() -> None:
    isolated_client = TestClient(app)
    response = isolated_client.get("/")
    cookies = response.cookies
    assert "cookie_consent" in cookies or "cookie_consent=" in response.headers.get(
        "set-cookie", ""
    )


def test_cors_allows_configured_origin() -> None:
    response = client.options(
        "/health",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.status_code in (200, 204)
    assert response.headers.get("access-control-allow-origin") == "http://localhost:3000"
