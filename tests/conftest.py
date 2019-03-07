import pytest

from inferkit.config import Config


@pytest.fixture
def config():
    return Config(api_key="test-key", model="test-model")
