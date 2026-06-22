import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Calculator Suite' in response.data

def test_basic_calculator_page(client):
    response = client.get('/calculator/basic')
    assert response.status_code == 200
    assert b'Basic Calculator' in response.data

def test_bmi_calculator_page(client):
    response = client.get('/calculator/bmi')
    assert response.status_code == 200
    assert b'BMI Calculator' in response.data

def test_converter_page(client):
    response = client.get('/calculator/converter')
    assert response.status_code == 200
    assert b'Unit Converter' in response.data

def test_basic_calculation_endpoint(client):
    response = client.post('/api/basic', json={
        'num1': 5,
        'num2': 3,
        'operation': '+'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['result'] == '8'

def test_bmi_endpoint(client):
    response = client.post('/api/bmi', json={
        'weight': 70,
        'height': 175
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert 'bmi' in data
    assert 'category' in data

def test_conversion_endpoint(client):
    response = client.post('/api/convert', json={
        'value': 1,
        'from_unit': 'm',
        'to_unit': 'cm',
        'category': 'length'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True
    assert data['result'] == '100'

def test_clear_history(client):
    response = client.post('/api/history/clear')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] == True