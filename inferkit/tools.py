"""Function-calling tools and dispatch."""

import inspect
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

from .errors import ToolError


@dataclass
class Tool:
    """A callable exposed to a model as a function tool."""

    name: str
    description: str
    function: Callable[..., Any]
    parameters: Dict[str, Any] = field(default_factory=dict)

    def schema(self) -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters or {"type": "object", "properties": {}},
            },
        }

    def invoke(self, arguments: Dict[str, Any]) -> Any:
        try:
            return self.function(**arguments)
        except TypeError as exc:
            raise ToolError(f"bad arguments for {self.name}: {exc}") from exc


def _json_type(annotation: Any) -> str:
    if annotation is str:
        return "string"
    if annotation is int:
        return "integer"
    if annotation is float:
        return "number"
    if annotation is bool:
        return "boolean"
    return "string"


def tool(name: str, description: str, parameters: Optional[Dict[str, Any]] = None):
    """Decorator that turns a function into a Tool."""

    def decorator(fn: Callable[..., Any]) -> Tool:
        schema = parameters
        if schema is None:
            hints = getattr(fn, "__annotations__", {})
            props = {
                key: {"type": _json_type(typ)}
                for key, typ in hints.items()
                if key != "return"
            }
            schema = {"type": "object", "properties": props}
        return Tool(name=name, description=description, function=fn, parameters=schema)

    return decorator


class Toolbox:
    """A registry of tools with JSON-schema based dispatch."""

    def __init__(self, tools: Optional[List[Tool]] = None):
        self._tools: Dict[str, Tool] = {t.name: t for t in tools or []}

    def register(self, tool: Tool) -> None:
        if tool.name in self._tools:
            raise ToolError(f"duplicate tool name: {tool.name}")
        self._tools[tool.name] = tool

    def schemas(self) -> List[Dict[str, Any]]:
        return [t.schema() for t in self._tools.values()]

    def call(self, name: str, arguments: Dict[str, Any]) -> Any:
        if name not in self._tools:
            raise ToolError(f"unknown tool: {name}")
        return self._tools[name].invoke(arguments)

    def __len__(self) -> int:
        return len(self._tools)
