from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_version():
    response = client.get("/version")

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == "translation-api"
    assert data["version"] == "1.0.0"