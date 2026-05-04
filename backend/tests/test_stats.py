from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_stats_returns_json():
    response = client.get("/api/stats")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
