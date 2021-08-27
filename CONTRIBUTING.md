# Contributing to inferkit

Thanks for your interest in contributing! This document covers the workflow
for reporting issues and opening pull requests.

## Getting started

1. Fork the repository and clone it locally.
2. Create a virtual environment and install the dev extras:
   `pip install -e ".[test,dev]"`.
3. Run the test suite with `pytest`.

## Development workflow

- Branch from `main` and use a descriptive branch name.
- Keep commits small and follow [Conventional Commits](https://www.conventionalcommits.org/).
- Add or update tests for any behaviour change.
- Run `ruff check .` and `pytest` before opening a pull request.

## Commit messages

Use the Conventional Commits format: `feat:`, `fix:`, `refactor:`, `test:`,
`docs:`, `chore:`, `build:`, `ci:`, and `perf:`.

## Pull requests

- Link the issue your change resolves.
- Describe what changed and why.
- Keep the diff focused; split unrelated changes into separate PRs.

