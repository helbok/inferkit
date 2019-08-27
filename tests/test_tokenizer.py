from inferkit.tokenizer import count_tokens, truncate_to_tokens


def test_count_tokens_positive():
    assert count_tokens("hello world") > 0


def test_truncate_short_text_unchanged():
    assert truncate_to_tokens("short", max_tokens=100) == "short"
