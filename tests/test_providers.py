from inferkit.providers import PROVIDER_REGISTRY


def test_registry_has_openai():
    assert "openai" in PROVIDER_REGISTRY


def test_registry_has_anthropic():
    assert "anthropic" in PROVIDER_REGISTRY
