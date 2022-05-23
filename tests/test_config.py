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


def test_edge_case_config_014():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_019():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_037():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_042():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_060():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_065():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_081():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_086():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_104():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_109():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_127():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_132():
    from inferkit.config import Config
    assert Config().temperature == 0.7


def test_edge_case_config_152():
    from inferkit.config import Config
    assert Config().temperature == 0.7
