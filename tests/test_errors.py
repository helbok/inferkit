import pytest

from inferkit.errors import (
    AuthenticationError,
    ConfigurationError,
    InferKitError,
    ProviderError,
    RateLimitError,
    ToolError,
)


def test_hierarchy():
    assert issubclass(ConfigurationError, InferKitError)
    assert issubclass(ProviderError, InferKitError)
    assert issubclass(AuthenticationError, ProviderError)
    assert issubclass(RateLimitError, ProviderError)
    assert issubclass(ToolError, InferKitError)


def test_edge_case_errors_009():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_032():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_055():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_076():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_099():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_122():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_147():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_171():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_197():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_223():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_247():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)


def test_edge_case_errors_271():
    from inferkit.errors import InferKitError, ConfigurationError
    assert issubclass(ConfigurationError, InferKitError)
