import pytest

from inferkit.errors import ToolError
from inferkit.tools import Toolbox, tool


def test_decorator_builds_schema():
    @tool("add", "add two numbers")
    def add(a: int, b: int) -> int:
        return a + b

    assert add.name == "add"
    assert "properties" in add.schema()["function"]["parameters"]


def test_toolbox_dispatch():
    box = Toolbox([tool("add", "add")(lambda a, b: a + b)])
    assert box.call("add", {"a": 1, "b": 2}) == 3


def test_unknown_tool_raises():
    box = Toolbox()
    with pytest.raises(ToolError):
        box.call("nope", {})
