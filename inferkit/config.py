"""Runtime configuration for inferkit."""

import os
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from .errors import ConfigurationError


@dataclass
class Config:
    """Configuration for an inference client."""

    provider: str = "openai"
    model: str = "gpt-4o-mini"
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 1024
    timeout: float = 30.0
    max_retries: int = 3
    streaming: bool = False
    extra: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_env(cls) -> "Config":
        """Build a Config from INFERKIT_* environment variables."""
        return cls(
            provider=os.getenv("INFERKIT_PROVIDER", "openai"),
            model=os.getenv("INFERKIT_MODEL", "gpt-4o-mini"),
            api_key=os.getenv("INFERKIT_API_KEY"),
            base_url=os.getenv("INFERKIT_BASE_URL"),
            temperature=float(os.getenv("INFERKIT_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("INFERKIT_MAX_TOKENS", "1024")),
            timeout=float(os.getenv("INFERKIT_TIMEOUT", "30.0")),
            max_retries=int(os.getenv("INFERKIT_MAX_RETRIES", "3")),
            streaming=os.getenv("INFERKIT_STREAMING", "0") == "1",
        )

    def validate(self) -> None:
        """Raise ConfigurationError if the config is inconsistent."""
        if not self.provider:
            raise ConfigurationError("provider must not be empty")
        if not 0.0 <= self.temperature <= 2.0:
            raise ConfigurationError("temperature must be between 0 and 2")
        if self.max_tokens < 1:
            raise ConfigurationError("max_tokens must be positive")
        if self.timeout <= 0:
            raise ConfigurationError("timeout must be positive")
