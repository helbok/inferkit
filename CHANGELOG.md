# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [3.4.0] - 2026-02-12

### Added

- Latency timer for observability
- numpy 2.0 support

## [3.0.0] - 2025-05-13

### Added

- One-shot completion from a prompt string
- Python 3.13 in CI

## [2.5.0] - 2024-09-26

### Added

- Cached top-k embedding search
- httpx 0.27 support

## [2.0.0] - 2024-03-05

### Added

- pydantic v2 support
- JSON-mode response parsing
- Python 3.12 in CI

### Changed

- Serialization now uses model_dump

## [1.5.0] - 2023-08-10

### Added

- Local llama.cpp provider
- Batch completions

## [1.0.0] - 2023-01-19

### Added

- Stable 1.0 public API
- Response text helper
- Python 3.8 minimum

### Fixed

- Empty provider names are rejected at validation

## [0.7.0] - 2022-07-06

### Added

- Async chat and streaming methods
- Python 3.11 in CI

## [0.6.0] - 2021-12-16

### Added

- Anthropic Messages provider
- Contributing guide and code of conduct

## [0.5.0] - 2021-06-03

### Added

- ReAct-style agent loop with tool dispatch
- Conversation memory integration for agents

## [0.4.0] - 2020-11-19

### Added

- Function-calling toolbox
- @tool decorator with annotation-based schemas

### Fixed

- Duplicate tool names are rejected at registration

## [0.3.0] - 2020-05-07

### Added

- Conversation memory with a sliding window
- Embedding similarity helpers
- Command-line interface
- Python 3.10 in CI

## [0.2.0] - 2019-10-24

### Added

- OpenAI-compatible provider
- Prompt templates and few-shot formatting
- Token counting with a fallback heuristic
- SSE parsing and streaming buffer

### Fixed

- Stream parser now ignores non-object events

## [0.1.0] - 2019-04-16

### Added

- Provider-agnostic inference client
- Typed request/response models
- Runtime configuration from environment variables
- Exception hierarchy for provider errors
