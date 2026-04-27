import pytest
from app import app

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_status():
    client = app.test_client()
    response = client.get("/status")

    assert response.status_code == 200
    assert response.json["status"] == "ok"

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_app_runs(client):
    """Teste que o app pode ser instanciado"""
    assert client is not None

def test_basic_route(client):
    """Teste uma rota básica - ajuste baseado nas suas rotas reais"""
    response = client.get('/')
    assert response.status_code in [200, 404]  # Ajuste baseado no seu app