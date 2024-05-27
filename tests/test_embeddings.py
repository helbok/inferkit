import pytest

from inferkit.embeddings import cosine_similarity, top_k_similar


def test_identical_vectors():
    assert cosine_similarity([1, 0], [1, 0]) == 1.0


def test_length_mismatch():
    with pytest.raises(ValueError):
        cosine_similarity([1, 0], [1, 0, 0])


def test_top_k_order():
    candidates = [("a", [1, 0]), ("b", [0, 1])]
    result = top_k_similar([1, 0], candidates, k=2)
    assert result[0][0] == "a"


def test_cached_top_k():
    from inferkit.embeddings import cached_top_k

    candidates = [("a", [1, 0]), ("b", [0, 1])]
    result = cached_top_k([1, 0], candidates, k=1)
    assert result[0][0] == "a"
