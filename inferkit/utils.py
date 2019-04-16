
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
