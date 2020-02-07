"""Command-line interface for inferkit."""

import argparse
import sys
from typing import List, Optional

from .client import InferenceClient
from .config import Config
from .model import Message


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="inferkit", description="LLM inference toolkit"
    )
    parser.add_argument("--provider", default=None, help="provider name")
    parser.add_argument("--model", default=None, help="model id")
    parser.add_argument("--max-tokens", type=int, default=None, help="token cap")
    parser.add_argument("--temperature", type=float, default=None, help="sampling")
    parser.add_argument("prompt", nargs="?", help="the prompt to send")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    config = Config.from_env()
    if args.provider:
        config.provider = args.provider
    if args.model:
        config.model = args.model
    client = InferenceClient(config)
    response = client.chat(
        messages=[Message(role="user", content=args.prompt or "Hello!")],
        max_tokens=args.max_tokens,
        temperature=args.temperature,
    )
    print(response.choices[0].message.content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
