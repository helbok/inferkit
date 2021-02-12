"""A minimal ReAct-style agent loop."""

import json
from dataclasses import dataclass
from typing import Optional

from .client import InferenceClient
from .errors import ToolError
from .memory import ConversationMemory
from .model import Message
from .tools import Toolbox


@dataclass
class AgentConfig:
    max_steps: int = 8
    verbose: bool = False
    system_prompt: str = "You are a helpful assistant that uses tools when needed."


class Agent:
    """An agent that can call tools while working toward a goal."""

    def __init__(
        self,
        client: InferenceClient,
        tools: Optional[Toolbox] = None,
        config: Optional[AgentConfig] = None,
    ):
        self.client = client
        self.toolbox = tools or Toolbox()
        self.config = config or AgentConfig()
        self.memory = ConversationMemory()

    def run(self, goal: str) -> str:
        """Run the agent loop and return the final assistant message."""
        self.memory.clear()
        self.memory.add(Message(role="system", content=self.config.system_prompt))
        self.memory.add_user(goal)

        for _ in range(self.config.max_steps):
            response = self.client.chat(
                messages=self.memory.to_list(),
                tools=self.toolbox.schemas() or None,
            )
            message = response.choices[0].message
            if message.tool_calls:
                for call in message.tool_calls:
                    name = call.function.get("name", "")
                    try:
                        args = json.loads(call.function.get("arguments") or "{}")
                        result = self.toolbox.call(name, args)
                    except (ToolError, json.JSONDecodeError, TypeError) as exc:
                        result = f"error: {exc}"
                    self.memory.add(Message(
                        role="tool",
                        content=str(result),
                        tool_call_id=call.id,
                    ))
            else:
                self.memory.add(Message(role="assistant", content=message.content))
                return message.content

        return "agent stopped after reaching the maximum number of steps"
