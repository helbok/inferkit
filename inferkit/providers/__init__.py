"""Provider registry for inferkit."""

from .base import Provider

PROVIDER_REGISTRY = {}

__all__ = ["Provider", "PROVIDER_REGISTRY"]
