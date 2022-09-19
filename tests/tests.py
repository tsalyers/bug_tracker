# A short set of tests for demo purposes. 
# Production ones would of course be quite a bit more extensive. 

import pytest
from ..app import app
from ..database.database_ops import execute_query

@pytest.fixture
def client():
    return app.test_client()

def test_database_connection():
    result = execute_query('select count(*) from users')
    assert result is not None

def test_get_bug_list(client):
    resp = client.get('/')
    assert 'Open Bug List' in resp.text
    assert resp.status_code == 200

def test_get_user_list(client):
    resp = client.get('/list_users')
    assert 'Users' in resp.text
    assert resp.status_code == 200