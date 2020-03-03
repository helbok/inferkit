from inferkit.cli import build_parser


def test_parser_defaults():
    parser = build_parser()
    args = parser.parse_args(["hello"])
    assert args.prompt == "hello"


def test_parser_model_flag():
    parser = build_parser()
    args = parser.parse_args(["--model", "m", "hi"])
    assert args.model == "m"
