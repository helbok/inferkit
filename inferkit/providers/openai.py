"""OpenAI-compatible provider (also works for many local gateways)."""

from typing import Iterator, Optional

import httpx

from ..errors import AuthenticationError, ProviderError, RateLimitError
from ..model import ModelRequest, ModelResponse
from .base import Provider


class OpenAIProvider(Provider):
    """Provider for the OpenAI chat-completions API."""

    name = "openai"
    DEFAULT_BASE_URL = "https://api.openai.com/v1"

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        super().__init__(api_key, base_url)
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}"}

    def _body(self, request: ModelRequest) -> dict:
        return request.dict(exclude_none=True)

    def complete(self, request: ModelRequest) -> ModelResponse:
        with httpx.Client(timeout=60.0) as http:
            resp = http.post(
                f"{self.base_url}/chat/completions",
                headers=self._headers(),
                json=self._body(request),
            )
        return self._handle(resp)

    def stream(self, request: ModelRequest) -> Iterator[str]:
        from ..streaming import extract_delta, parse_sse

        with httpx.Client(timeout=60.0) as http:
            with http.stream(
                "POST",
                f"{self.base_url}/chat/completions",
                headers=self._headers(),
                json=self._body(request),
            ) as resp:
                if resp.status_code >= 400:
                    raise self._error_for(resp.status_code)
                for line in resp.iter_lines():
                    for event in parse_sse(line):
                        if event.get("done"):
                            return
                        delta = extract_delta(event)
                        if delta:
                            yield delta

    @staticmethod
    def _handle(resp: httpx.Response) -> ModelResponse:
        if resp.status_code == 401:
            raise AuthenticationError("invalid API key")
        if resp.status_code == 429:
            raise RateLimitError("rate limit exceeded")
        if resp.status_code >= 400:
            raise ProviderError(f"provider returned {resp.status_code}")
        return ModelResponse(**resp.json())

    @staticmethod
    def _error_for(status: int) -> Exception:
        if status == 401:
            return AuthenticationError("invalid API key")
        if status == 429:
            return RateLimitError("rate limit exceeded")
        return ProviderError(f"provider returned {status}")
