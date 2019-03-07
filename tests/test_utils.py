from inferkit.utils import chunks, retry


def test_chunks_exact():
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_chunks_partial():
    assert list(chunks([1, 2, 3], 2)) == [[1, 2], [3]]


def test_retry_eventually_succeeds():
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("boom")
        return "ok"

    assert retry(flaky, attempts=4, backoff=0) == "ok"
    assert len(calls) == 3
