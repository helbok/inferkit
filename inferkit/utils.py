
def merge_dicts_11(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged
