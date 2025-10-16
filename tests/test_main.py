from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_check_member_exists():
    response = client.get("/check-member/jazmin")
    assert response.status_code == 200
    assert response.json()["registered"] is True

def test_check_member_not_found():
    response = client.get("/check-member/juan")
    assert response.status_code == 200
    assert response.json()["registered"] is False
    