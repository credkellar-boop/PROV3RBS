from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_proverb_endpoint():
    response = client.get("/api/proverb")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "text" in response.json()["data"]

def test_localization_rendering():
    response = client.get("/?lang=es")
    assert response.status_code == 200
    assert b"PROV3RBS" in response.content
  
