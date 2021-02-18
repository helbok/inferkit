from inferkit.agent import Agent, AgentConfig
from inferkit.client import InferenceClient
from inferkit.config import Config
from inferkit.model import ModelResponse


class FakeProvider:
    def complete(self, request):
        return ModelResponse(
            model=request.model,
            choices=[{"index": 0, "message": {"role": "assistant", "content": "done"}}],
        )

    def stream(self, request):
        return iter(["done"])


def test_agent_returns_without_tools():
    client = InferenceClient(Config(api_key="k"), provider=FakeProvider())
    agent = Agent(client, config=AgentConfig(max_steps=2))
    assert agent.run("hi") == "done"
