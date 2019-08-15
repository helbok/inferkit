import pytest

from inferkit.prompts import PromptTemplate, chat_messages, format_few_shot


def test_template_render():
    tpl = PromptTemplate("hello {name}")
    assert tpl.render(name="bob") == "hello bob"


def test_template_missing_variable():
    tpl = PromptTemplate("hello {name}")
    with pytest.raises(ValueError):
        tpl.render()


def test_chat_messages_order():
    msgs = chat_messages("sys", "user")
    assert [m.role for m in msgs] == ["system", "user"]


def test_few_shot_format():
    text = format_few_shot([{"input": "a", "output": "b"}])
    assert "Example 1" in text
