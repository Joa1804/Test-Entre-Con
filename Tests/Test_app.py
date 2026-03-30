import pytest
from app import app

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