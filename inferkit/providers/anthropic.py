"""Anthropic Messages API provider."""

from typing import Iterator, Optional

import httpx

from ..errors import AuthenticationError, ProviderError, RateLimitError
from ..model import Choice, Message, ModelRequest, ModelResponse
from .base import Provider


class AnthropicProvider(Provider):
    """Provider for the Anthropic Messages API."""

    name = "anthropic"
    DEFAULT_BASE_URL = "https://api.anthropic.com/v1"
    VERSION = "2023-06-01"

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        super().__init__(api_key, base_url)
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")

    def _payload(self, request: ModelRequest) -> dict:
        system = []
        messages = []
        for m in request.messages:
            if m.role == "system":
                system.append(m.content)
            else:
                messages.append({"role": m.role, "content": m.content})
        payload = {
            "model": request.model,
            "max_tokens": request.max_tokens or 1024,
            "messages": messages,
            "temperature": request.temperature,
        }
        if system:
            payload["system"] = "\n".join(system)
        return payload

    def complete(self, request: ModelRequest) -> ModelResponse:
        payload = self._payload(request)
        with httpx.Client(timeout=60.0) as http:
            resp = http.post(
                f"{self.base_url}/messages",
                headers={
                    "x-api-key": self.api_key or "",
                    "anthropic-version": self.VERSION,
                    "content-type": "application/json",
                },
                json=payload,
            )
        if resp.status_code == 401:
            raise AuthenticationError("invalid API key")
        if resp.status_code == 429:
            raise RateLimitError("rate limit exceeded")
        if resp.status_code >= 400:
            raise ProviderError(f"provider returned {resp.status_code}")
        data = resp.json()
        text = "".join(block.get("text", "") for block in data.get("content", []))
        return ModelResponse(
            id=data.get("id"),
            model=data.get("model"),
            choices=[Choice(
                message=Message(role="assistant", content=text),
                finish_reason=data.get("stop_reason"),
            )],
        )

    def stream(self, request: ModelRequest) -> Iterator[str]:
        payload = self._payload(request)
        payload["stream"] = True
        with httpx.Client(timeout=60.0) as http:
            with http.stream(
                "POST", f"{self.base_url}/messages", json=payload,
                headers={"x-api-key": self.api_key or "",
                         "anthropic-version": self.VERSION,
                         "content-type": "application/json"},
            ) as resp:
                if resp.status_code >= 400:
                    raise ProviderError(f"provider returned {resp.status_code}")
                for line in resp.iter_lines():
                    if line.startswith("data:") and line[5:].strip():
                        import json
                        event = json.loads(line[5:].strip())
                        if event.get("type") == "content_block_delta":
                            yield event.get("delta", {}).get("text", "")
