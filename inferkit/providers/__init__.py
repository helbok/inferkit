"""Provider registry for inferkit."""

from .anthropic import AnthropicProvider
from .base import Provider
from .openai import OpenAIProvider

PROVIDER_REGISTRY = {"openai": OpenAIProvider, "anthropic": AnthropicProvider}

__all__ = ["Provider", "OpenAIProvider", "AnthropicProvider", "PROVIDER_REGISTRY"]
