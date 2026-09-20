"""API health tests."""

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_root_endpoint() -> None:
    """Root endpoint should return service information."""

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health_endpoint() -> None:
    """Health endpoint should report healthy status."""

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
