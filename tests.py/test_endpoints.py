from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_login():
    response = client.post("/login", data={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()