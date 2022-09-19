import pytest
from ..app import create_app
from ..database.database_ops import execute_query

@pytest.fixture
def app():
    app = create_app()
    return app