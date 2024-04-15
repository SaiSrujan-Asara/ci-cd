import pytest
from hello_app.webapp import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home' in response.data


def test_api_data_route(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    
