"""Streaming helpers: SSE parsing and delta extraction."""

import json
from typing import Any, Dict, Iterator, Optional


def parse_sse(chunk: str) -> Iterator[Dict[str, Any]]:
    """Parse a raw SSE chunk into individual JSON events."""
    for line in chunk.splitlines():
        if not line or line.startswith(":"):
            continue
        if line.startswith("data:"):
            payload = line[5:].strip()
            if payload == "[DONE]":
                yield {"done": True}
                continue
            try:
                yield json.loads(payload)
            except json.JSONDecodeError:
                continue


def extract_delta(event: Dict[str, Any]) -> str:
    """Extract the text delta from an OpenAI-style streaming event."""
    if not isinstance(event, dict):
        return ""
    choices = event.get("choices") or []
    if not choices:
        return ""
    delta = choices[0].get("delta") or {}
    return delta.get("content") or ""


class StreamBuffer:
    """Accumulate deltas and emit complete chunks when possible."""

    def __init__(self, chunk_size: int = 4096):
        self.chunk_size = chunk_size
        self._buf = ""

    def feed(self, text: str) -> Optional[str]:
        """Feed text; return a full chunk once the buffer is large enough."""
        if not text:
            return None
        self._buf += text
        if len(self._buf) >= self.chunk_size:
            out, self._buf = self._buf, ""
            return out
        return None

    def flush(self) -> str:
        """Return and clear any remaining buffered text."""
        out, self._buf = self._buf, ""
        return out
