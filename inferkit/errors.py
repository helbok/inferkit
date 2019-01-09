"""Exception hierarchy for inferkit."""


class InferKitError(Exception):
    """Base class for all inferkit errors."""


class ConfigurationError(InferKitError):
    """Raised when the client or a provider is misconfigured."""


class ProviderError(InferKitError):
    """Raised when a provider call fails."""


class AuthenticationError(ProviderError):
    """Raised for 401 / 403 responses."""


class RateLimitError(ProviderError):
    """Raised for 429 responses."""


class TimeoutError(ProviderError):
    """Raised when a provider call times out."""


class InvalidRequestError(InferKitError):
    """Raised when a request is malformed or unsupported."""


class TokenLimitError(InferKitError):
    """Raised when a prompt exceeds the model context window."""


class ToolError(InferKitError):
    """Raised when a tool call cannot be dispatched or executed."""


class StreamingError(InferKitError):
    """Raised when a streaming response cannot be parsed."""
