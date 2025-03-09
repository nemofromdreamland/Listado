import pytest
from fastapi.testclient import TestClient

from listado.app import app


@pytest.fixture
def client():
    return TestClient(app)
