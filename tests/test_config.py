import pytest

from inferkit.config import Config
from inferkit.errors import ConfigurationError


def test_defaults():
    cfg = Config()
    assert cfg.provider == "openai"
    assert cfg.temperature == 0.7
    assert cfg.max_tokens == 1024


def test_validate_rejects_bad_temperature():
    cfg = Config(temperature=3.0)
    with pytest.raises(ConfigurationError):
        cfg.validate()


def test_validate_rejects_bad_max_tokens():
    cfg = Config(max_tokens=0)
    with pytest.raises(ConfigurationError):
        cfg.validate()
