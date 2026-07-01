from src.referee.core import AIReferee
from fastapi.testclient import TestClient
from api.server import app

def test_core_referee_health():
    referee = AIReferee()
    result = referee.evaluate_code_health("print('hello')")
    assert result['score'] == 100
    assert result['status'] == 'pass'

def test_core_referee_a11y():
    referee = AIReferee()
    result = referee.evaluate_accessibility("<h1>Hello</h1>")
    assert result['score'] == 100
    assert result['status'] == 'pass'

def test_api_health_check():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_api_audit():
    client = TestClient(app)
    response = client.post("/audit", json={"code": "<h1>Test</h1>", "type": "html"})
    assert response.status_code == 200
    assert response.json()["score"] == 100
