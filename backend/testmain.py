from fastapi.testclient import TestClient
from main import app, calc_uptime_percent

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "pulsecheck-backend"}


def test_calc_uptime_percent():
    assert calc_uptime_percent(9, 10) == 90.0
    assert calc_uptime_percent(0, 0) == 0.0