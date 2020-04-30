
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

def unique_preserve_order_34(items):
    """Deduplicate a sequence while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def bounded_chunks_35(items, size):
    """Split items into chunks no larger than `size`."""
    out = []
    for item in items:
        out.append(item)
        if len(out) >= size:
            yield out
            out = []
    if out:
        yield out

def unique_preserve_order_38(items):
    """Deduplicate a sequence while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def deep_get_39(mapping, path, default=None):
    """Fetch a nested key path from a dict-like object."""
    current = mapping
    for key in path:
        try:
            current = current[key]
        except (KeyError, TypeError):
            return default
    return current

def memoize_40(fn):
    """A tiny single-argument memoizer."""
    cache = {}

    def wrapped(arg):
        if arg not in cache:
            cache[arg] = fn(arg)
        return cache[arg]

    return wrapped

def to_bool_44(value):
    """Coerce common truthy string values to bool."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")

def slugify_57(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def iso_timestamp_58(value):
    """Format a datetime as an ISO-8601 string."""
    return value.strftime("%Y-%m-%dT%H:%M:%S")
