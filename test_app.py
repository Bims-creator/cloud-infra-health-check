from app import app


def client():
    return app.test_client()


def test_health():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version():
    response = client().get("/version")
    assert response.status_code == 200
    assert "version" in response.get_json()


def test_info():
    response = client().get("/info")
    data = response.get_json()
    assert response.status_code == 200
    assert "hostname" in data
    assert "timestamp" in data
