"""The main inference client and provider registry facade."""

from typing import Iterator, List, Optional

from .config import Config
from .errors import ConfigurationError
from .model import Message, ModelRequest, ModelResponse
from .providers.base import Provider


class InferenceClient:
    """A thin, provider-agnostic facade over model backends."""

    def __init__(self, config: Config = None, provider: Provider = None):
        self.config = config or Config.from_env()
        self.provider = provider or self._make_provider(self.config)

    @staticmethod
    def _make_provider(config: Config) -> Provider:
        from .providers import PROVIDER_REGISTRY

        cls = PROVIDER_REGISTRY.get(config.provider)
        if cls is None:
            raise ConfigurationError(f"unknown provider: {config.provider}")
        return cls(api_key=config.api_key, base_url=config.base_url)

    def chat(
        self,
        messages: List[Message],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        tools: Optional[List[dict]] = None,
    ) -> ModelResponse:
        """Run one chat completion."""
        request = ModelRequest(
            model=model or self.config.model,
            messages=messages,
            temperature=temperature if temperature is not None else self.config.temperature,
            max_tokens=max_tokens or self.config.max_tokens,
            tools=tools,
        )
        return self.provider.complete(request)

    def stream(
        self,
        messages: List[Message],
        model: Optional[str] = None,
        **kwargs,
    ) -> Iterator[str]:
        """Stream a chat completion as an iterator of text deltas."""
        request = ModelRequest(
            model=model or self.config.model,
            messages=messages,
            stream=True,
            **kwargs,
        )
        return self.provider.stream(request)
