import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_task_integration(client):
    response = client.post('/add', data={'task': 'Integration task'}, follow_redirects=True)
    assert b'Integration task' in response.data