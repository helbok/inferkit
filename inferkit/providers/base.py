"""Provider interface for inferkit."""

from abc import ABC, abstractmethod
from typing import AsyncIterator, Iterator, Optional

from ..model import ModelRequest, ModelResponse


class Provider(ABC):
    """Abstract base class for model providers."""

    name: str = "base"

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url

    @abstractmethod
    def complete(self, request: ModelRequest) -> ModelResponse:
        """Run a single non-streaming completion."""

    def stream(self, request: ModelRequest) -> Iterator[str]:
        """Yield completion text incrementally. Defaults to non-streaming."""
        response = self.complete(request)
        for choice in response.choices:
            yield choice.message.content

    async def acomplete(self, request: ModelRequest) -> ModelResponse:
        """Async completion; defaults to the sync implementation."""
        return self.complete(request)

    async def astream(self, request: ModelRequest) -> AsyncIterator[str]:
        """Async streaming; defaults to iterating the sync stream."""
        for token in self.stream(request):
            yield token
