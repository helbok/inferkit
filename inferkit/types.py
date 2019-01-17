"""Shared type aliases used across inferkit."""

from typing import Any, Dict, List, Union

JSON = Union[Dict[str, Any], List[Any], str, int, float, bool, None]
MessageRole = str
ProviderName = str
