"""Typed request/response models for inference calls."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    """A single chat message."""

    role: str = Field(..., description="system, user, assistant or tool.")
    content: str = ""
    name: Optional[str] = None
    tool_calls: Optional[List["ToolCall"]] = None
    tool_call_id: Optional[str] = None


class ToolCall(BaseModel):
    """A function-call request emitted by a model."""

    id: str
    type: str = "function"
    function: Dict[str, Any] = Field(default_factory=dict)


class ModelRequest(BaseModel):
    """A completion request."""

    model: str
    messages: List[Message]
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    stream: bool = False
    tools: Optional[List[Dict[str, Any]]] = None
    stop: Optional[List[str]] = None


class Usage(BaseModel):
    """Token accounting for a completion."""

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class Choice(BaseModel):
    """One candidate completion."""

    index: int = 0
    message: Message = Field(default_factory=lambda: Message(role="assistant"))
    finish_reason: Optional[str] = None


class ModelResponse(BaseModel):
    """A completion response."""

    id: Optional[str] = None
    model: Optional[str] = None
    choices: List[Choice] = Field(default_factory=list)
    usage: Optional[Usage] = None
    created: Optional[int] = None


Message.update_forward_refs()
