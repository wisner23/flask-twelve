import pytest

from app import app


@pytest.fixture
def application():
    return app
