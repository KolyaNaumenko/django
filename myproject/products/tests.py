from django.test import TestCase
import pytest
from myproject  import manage  # Імпортуємо WSGI для тестування Django

@pytest.fixture
def client():
    from django.test.client import Client
    return Client()

def test_products_endpoint(client):
    response = client.get('/products/1')
    assert response.status_code == 200
    assert response.json() == {"id": "1", "name": "1 name"}
# Create your tests here.
