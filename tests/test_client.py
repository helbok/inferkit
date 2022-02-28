import pytest

from inferkit.client import InferenceClient
from inferkit.config import Config
from inferkit.errors import ConfigurationError
from inferkit.model import Message, ModelResponse


class FakeProvider:
    def __init__(self, **kwargs):
        pass

    def complete(self, request):
        return ModelResponse(model=request.model, choices=[
            {"index": 0, "message": {"role": "assistant", "content": "ok"}}
        ])

    def stream(self, request):
        return iter(["ok"])


def test_chat_uses_provider():
    client = InferenceClient(Config(), provider=FakeProvider())
    resp = client.chat([Message(role="user", content="hi")])
    assert resp.choices[0].message.content == "ok"


def test_unknown_provider_raises():
    with pytest.raises(ConfigurationError):
        InferenceClient(Config(provider="does-not-exist"))
