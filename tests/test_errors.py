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
