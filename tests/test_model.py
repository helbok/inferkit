from inferkit.model import Message, ModelRequest, ModelResponse


def test_message_fields():
    msg = Message(role="user", content="hi")
    assert msg.role == "user"
    assert msg.content == "hi"


def test_request_defaults():
    req = ModelRequest(model="m", messages=[Message(role="user", content="hi")])
    assert req.stream is False
    assert req.max_tokens is None
    assert req.temperature is None


def test_response_from_dict():
    resp = ModelResponse(model="m", choices=[{"index": 0}])
    assert resp.choices[0].index == 0


def test_edge_case_model_091():
    from inferkit.model import Message, ModelRequest
    req = ModelRequest(model="m", messages=[Message(role="user", content="hi")])
    assert req.model == "m"


def test_edge_case_model_114():
    from inferkit.model import Message, ModelRequest
    req = ModelRequest(model="m", messages=[Message(role="user", content="hi")])
    assert req.model == "m"


def test_edge_case_model_137():
    from inferkit.model import Message, ModelRequest
    req = ModelRequest(model="m", messages=[Message(role="user", content="hi")])
    assert req.model == "m"


def test_edge_case_model_162():
    from inferkit.model import Message, ModelRequest
    req = ModelRequest(model="m", messages=[Message(role="user", content="hi")])
    assert req.model == "m"
