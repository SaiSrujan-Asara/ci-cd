import pytest
from webapp import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home' in response.data

def test_about_route(client):
    response = client.get('/about/')
    assert response.status_code == 200
    assert b'About us' in response.data

def test_contact_route(client):
    response = client.get('/contact/')
    assert response.status_code == 200
    assert b'Contact us' in response.data

def test_hello_route(client):
    response = client.get('/hello/')
    assert response.status_code == 200
    assert b'Hello, CI/CD' in response.data

def test_api_data_route(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    
