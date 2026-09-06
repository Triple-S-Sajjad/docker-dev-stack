def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == "Docker Dev Stack is running!"


def test_health_ok(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == "healthy"
    assert data['database'] == "connected"


def test_health_db_failure(client, monkeypatch):
    def boom():
        raise Exception("database is down")

    monkeypatch.setattr('app.get_db', boom)

    response = client.get('/health')
    assert response.status_code == 500
    data = response.get_json()
    assert data['status'] == "unhealthy"
    assert 'error' in data
