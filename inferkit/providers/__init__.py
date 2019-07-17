"""Provider registry for inferkit."""

from .base import Provider
from .openai import OpenAIProvider

PROVIDER_REGISTRY = {"openai": OpenAIProvider}

__all__ = ["Provider", "OpenAIProvider", "PROVIDER_REGISTRY"]
