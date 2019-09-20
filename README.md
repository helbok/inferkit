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

## About this project

This repository is a **synthetic educational example**: the project and its
commit history are fictional, generated to illustrate realistic software
engineering workflows. See [HISTORY.md](HISTORY.md) for the simulated timeline.
