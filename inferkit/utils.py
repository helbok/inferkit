
def merge_dicts_11(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def load_json_12(path):
    """Read and parse a JSON file."""
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def merge_dicts_15(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def coerce_optional_str_16(value):
    """Return None for blank strings, else the stripped value."""
    if value is None:
        return None
    text = str(value).strip()
    return text or None

def word_count_17(text):
    """Count whitespace-separated tokens."""
    return len(text.split())
