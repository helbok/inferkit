"""inferkit: a lightweight toolkit for LLM inference and agent workflows."""

__version__ = "0.5.0"

from .agent import Agent, AgentConfig
from .client import InferenceClient
from .config import Config
from .embeddings import cosine_similarity
from .errors import InferKitError
from .memory import ConversationMemory
from .model import Message, ModelRequest, ModelResponse, Usage
from .prompts import PromptTemplate
from .tools import Tool, Toolbox, tool

__all__ = [
    "Agent",
    "AgentConfig",
    "InferenceClient",
    "Config",
    "cosine_similarity",
    "InferKitError",
    "ConversationMemory",
    "Message",
    "ModelRequest",
    "ModelResponse",
    "Usage",
    "PromptTemplate",
    "Tool",
    "Toolbox",
    "tool",
]
