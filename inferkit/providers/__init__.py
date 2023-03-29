"""Provider registry for inferkit."""

from .anthropic import AnthropicProvider
from .base import Provider
from .local import LocalProvider
from .openai import OpenAIProvider

PROVIDER_REGISTRY = {
    "openai": OpenAIProvider,
    "anthropic": AnthropicProvider,
    "local": LocalProvider,
}

__all__ = [
    "Provider",
    "OpenAIProvider",
    "AnthropicProvider",
    "LocalProvider",
    "PROVIDER_REGISTRY",
]
