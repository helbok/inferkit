"""Prompt templates and formatting helpers."""

from typing import Dict, List, Mapping, Optional

from .model import Message


class PromptTemplate:
    """A simple {placeholder} template with a safe renderer."""

    def __init__(self, template: str):
        self.template = template

    def render(self, **kwargs) -> str:
        try:
            return self.template.format_map(kwargs)
        except KeyError as exc:
            missing = exc.args[0]
            raise ValueError(f"missing template variable: {missing}") from exc


SYSTEM_TEMPLATES: Dict[str, PromptTemplate] = {
    "assistant": PromptTemplate(
        "You are {name}, a helpful assistant. Be concise and accurate."
    ),
    "coder": PromptTemplate(
        "You are an expert software engineer. Prefer correct, tested code."
    ),
    "summarizer": PromptTemplate(
        "Summarize the following text in {length} words or fewer."
    ),
}


def chat_messages(
    system: str,
    user: str,
    history: Optional[List[Message]] = None,
) -> List[Message]:
    """Build a message list from a system prompt and a user turn."""
    msgs = [Message(role="system", content=system)]
    for msg in history or []:
        msgs.append(msg)
    msgs.append(Message(role="user", content=user))
    return msgs


def format_few_shot(examples: List[Mapping[str, str]]) -> str:
    """Render few-shot examples as a numbered block."""
    lines = []
    for i, ex in enumerate(examples, 1):
        lines.append(f"Example {i}:")
        lines.append(f"  Input: {ex['input']}")
        lines.append(f"  Output: {ex['output']}")
    return "\n".join(lines)
