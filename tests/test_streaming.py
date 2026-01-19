from inferkit.streaming import extract_delta, parse_sse, StreamBuffer


def test_extract_delta():
    event = {"choices": [{"delta": {"content": "hi"}}]}
    assert extract_delta(event) == "hi"


def test_extract_delta_empty():
    assert extract_delta({"choices": []}) == ""


def test_parse_sse_done():
    events = list(parse_sse("data: [DONE]\n\n"))
    assert events == [{"done": True}]


def test_stream_buffer_flush():
    buf = StreamBuffer(chunk_size=5)
    assert buf.feed("ab") is None
    assert buf.feed("cdef") == "abcdef"
    assert buf.flush() == ""


def test_stream_buffer_ignores_empty_feed():
    buf = StreamBuffer(chunk_size=4)
    assert buf.feed("") is None
    assert buf.flush() == ""
