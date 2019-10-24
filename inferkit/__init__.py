"""inferkit: a lightweight toolkit for LLM inference and agent workflows."""

__version__ = "0.2.0"

from .client import InferenceClient
from .config import Config
from .errors import InferKitError
from .model import Message, ModelRequest, ModelResponse, Usage

__all__ = [
    "InferenceClient",
    "Config",
    "InferKitError",
    "Message",
    "ModelRequest",
    "ModelResponse",
    "Usage",
]
