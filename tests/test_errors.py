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
