"""Local model provider that talks to a llama.cpp HTTP server."""

from typing import Iterator, Optional

import httpx

from ..errors import ProviderError
from ..model import Choice, Message, ModelRequest, ModelResponse
from .base import Provider


class LocalProvider(Provider):
    """Provider for a self-hosted llama.cpp server."""

    name = "local"
    DEFAULT_BASE_URL = "http://127.0.0.1:8080"

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        super().__init__(api_key, base_url)
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")

    @staticmethod
    def _render_prompt(request: ModelRequest) -> str:
        parts = []
        for m in request.messages:
            parts.append(f"{m.role.upper()}: {m.content}")
        parts.append("ASSISTANT:")
        return "\n".join(parts)

    def complete(self, request: ModelRequest) -> ModelResponse:
        prompt = self._render_prompt(request)
        try:
            with httpx.Client(timeout=120.0) as http:
                resp = http.post(
                    f"{self.base_url}/completion",
                    json={
                        "prompt": prompt,
                        "n_predict": request.max_tokens or 256,
                        "temperature": request.temperature or 0.8,
                    },
                )
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise ProviderError(f"local server unreachable: {exc}") from exc
        text = resp.json().get("content", "")
        return ModelResponse(
            model=request.model,
            choices=[Choice(
                message=Message(role="assistant", content=text),
                finish_reason="stop",
            )],
        )

    def stream(self, request: ModelRequest) -> Iterator[str]:
        prompt = self._render_prompt(request)
        try:
            with httpx.Client(timeout=120.0) as http:
                with http.stream(
                    "POST",
                    f"{self.base_url}/completion",
                    json={"prompt": prompt, "stream": True,
                          "n_predict": request.max_tokens or 256,
                          "temperature": request.temperature or 0.8},
                ) as resp:
                    resp.raise_for_status()
                    for line in resp.iter_lines():
                        if line.startswith("data:"):
                            import json
                            event = json.loads(line[5:].strip())
                            yield event.get("content", "")
        except httpx.HTTPError as exc:
            raise ProviderError(f"local server unreachable: {exc}") from exc
