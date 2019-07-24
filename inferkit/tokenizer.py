"""Token counting via tiktoken with a dependency-free fallback."""

from functools import lru_cache
from typing import Optional

try:  # pragma: no cover - exercised when tiktoken is installed
    import tiktoken
except ImportError:  # pragma: no cover
    tiktoken = None

DEFAULT_ENCODING = "cl100k_base"


@lru_cache(maxsize=None)
def _get_encoding(name: str):
    if tiktoken is None:
        return None
    return tiktoken.get_encoding(name)


def count_tokens(text: str, encoding: str = DEFAULT_ENCODING) -> int:
    """Return the number of tokens in `text`."""
    enc = _get_encoding(encoding)
    if enc is not None:
        return len(enc.encode(text))
    return max(1, len(text) // 4)


def truncate_to_tokens(
    text: str,
    max_tokens: int,
    encoding: str = DEFAULT_ENCODING,
) -> str:
    """Truncate `text` so it fits within `max_tokens`."""
    enc = _get_encoding(encoding)
    if enc is None:
        return text[: max_tokens * 4]
    tokens = enc.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return enc.decode(tokens[:max_tokens])
