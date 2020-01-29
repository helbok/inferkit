"""Embedding helpers: similarity and nearest-neighbour search."""

import math
from typing import List, Sequence, Tuple


def cosine_similarity(a: Sequence[float], b: Sequence[float]) -> float:
    """Cosine similarity between two equal-length vectors."""
    if len(a) != len(b):
        raise ValueError("vectors must have the same length")
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def top_k_similar(
    query: Sequence[float],
    candidates: Sequence[Tuple[str, Sequence[float]]],
    k: int = 5,
) -> List[Tuple[str, float]]:
    """Return the `k` candidates most similar to `query`."""
    scored = sorted(
        ((key, cosine_similarity(query, vec)) for key, vec in candidates),
        key=lambda pair: pair[1],
        reverse=True,
    )
    return scored[:k]
