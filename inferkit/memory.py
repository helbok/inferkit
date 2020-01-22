"""Conversation memory for agent sessions."""

from collections import deque
from typing import Deque, List

from .model import Message


class ConversationMemory:
    """A bounded sliding window of conversation messages."""

    def __init__(self, max_messages: int = 20):
        self.max_messages = max_messages
        self._messages: Deque[Message] = deque()

    def add(self, message: Message) -> None:
        """Append a message, evicting the oldest when over capacity."""
        self._messages.append(message)
        while len(self._messages) > self.max_messages:
            self._messages.popleft()

    def add_user(self, content: str) -> None:
        self.add(Message(role="user", content=content))

    def add_assistant(self, content: str) -> None:
        self.add(Message(role="assistant", content=content))

    def clear(self) -> None:
        self._messages.clear()

    def to_list(self) -> List[Message]:
        return list(self._messages)

    def __len__(self) -> int:
        return len(self._messages)
