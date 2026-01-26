# inferkit

A lightweight Python toolkit for LLM inference, prompting, and agent
workflows. `inferkit` provides a provider-agnostic client, request/response
models, prompt templates, token counting, streaming helpers, embeddings
utilities, and a small agent loop with function-calling tools.

## Installation

```console
$ pip install inferkit
```

Install from source with the test and development extras:

```console
$ pip install -e ".[test,dev]"
```

## Quick start

```python
from inferkit import InferenceClient, Message

client = InferenceClient()
resp = client.chat([Message(role="user", content="Hello!")])
print(resp.choices[0].message.content)
```

Set the provider and model through configuration or environment variables:

```console
$ export INFERKIT_PROVIDER=openai
$ export INFERKIT_MODEL=gpt-4o-mini
```

## Features

- **Provider-agnostic client** -- one API over OpenAI-compatible, Anthropic
  and local backends.
- **Typed models** -- pydantic models for requests, responses, messages and
  usage accounting.
- **Prompt templates** -- reusable system-prompt templates and few-shot
  formatting.
- **Token counting** -- accurate token counts via `tiktoken` with a
  dependency-free fallback.
- **Streaming** -- SSE parsing and incremental delta extraction.
- **Tools and agents** -- a function-calling toolbox and a ReAct-style agent
  loop with conversation memory.

## Architecture

The package is layered: `client` owns the provider-agnostic facade, `model`
holds the request/response types, `providers` adapts each backend to a common
interface, and the higher-level modules (`prompts`, `tools`, `agent`, `memory`)
build on top.

```text
cli / agent
    |
  client  ------ providers (openai, anthropic, local)
    |
  model / streaming / tokenizer
```

## Development

```console
$ pip install -e ".[test,dev]"
$ pytest
$ ruff check .
```

## Providers

`inferkit` ships with an OpenAI-compatible provider out of the box. Set
`INFERKIT_PROVIDER` (or pass a `Config`) to select the backend, and
`INFERKIT_BASE_URL` to point at a compatible gateway. Providers implement a
common `complete` / `stream` interface, so application code does not change
when you swap backends.

## Tools

Tools expose Python functions to a model as JSON-schema function calls. Use
the `@tool` decorator to describe a function, register it in a `Toolbox`, and
pass `Toolbox.schemas()` to a chat request. The model can then request tool
calls, which `Toolbox.call` dispatches safely.

## Agents

`Agent` runs a ReAct-style loop: it sends the goal to the model, dispatches any
requested tool calls through a `Toolbox`, feeds the results back, and returns
the final assistant message once the model stops calling tools. Configure the
step budget and system prompt with `AgentConfig`.

## Async usage

Every synchronous call has an asynchronous twin. `achat` and `astream` run the
same request through the provider's async path, which is useful inside
`asyncio` servers and pipelines.

## Error handling

Provider failures map to a small, typed hierarchy: `AuthenticationError` for
bad credentials, `RateLimitError` for 429s, and `ProviderError` for anything
else. Catch `InferKitError` to handle every inferkit failure uniformly, or the
specific subclasses to react differently.

## Local models

The `local` provider talks to a self-hosted llama.cpp HTTP server. Point
`INFERKIT_BASE_URL` at the server and select the `local` provider to run models
without any external API dependency.

## Structured output

For JSON-mode responses, `parse_json_response` decodes the first choice's
content and returns `None` when the model produces invalid JSON, so callers can
fall back gracefully instead of crashing.

## Embeddings

`cosine_similarity` and `top_k_similar` cover the common retrieval cases, and
`cached_top_k` adds a small result cache for repeated queries against a fixed
candidate set.

## Retry policies

Transient failures are common with hosted models. `Config.max_retries` controls
how many attempts a client makes, and `inferkit.utils.retry` provides a small
backoff helper for wrapping your own calls.

## Observability

Use `inferkit.utils.log_event` for structured log lines and `Timer` to measure
request latency around inference calls. Both compose cleanly with standard
logging and tracing setups.

## Security

Never commit API keys. Load them from environment variables or a secret
manager, and treat model output as untrusted input inside your application.

## License

MIT -- see the LICENSE file for the full text.

## About this project

This repository is a **synthetic educational example**: the project and its
commit history are fictional, generated to illustrate realistic software
engineering workflows. See [HISTORY.md](HISTORY.md) for the simulated timeline.
