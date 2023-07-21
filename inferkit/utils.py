
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

def slugify_61(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def safe_float_62(value, default=0.0):
    """Parse a float, returning a default on failure."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def first_non_none_63(values):
    """Return the first non-None value, short-circuiting."""
    for value in values:
        if value is not None:
            return value
    return None

def merge_dicts_67(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def load_json_68(path):
    """Read and parse a JSON file."""
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def unique_preserve_order_78(items):
    """Deduplicate a sequence while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def bounded_chunks_79(items, size):
    """Split items into chunks no larger than `size`."""
    out = []
    for item in items:
        out.append(item)
        if len(out) >= size:
            yield out
            out = []
    if out:
        yield out

def unique_preserve_order_82(items):
    """Deduplicate a sequence while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def deep_get_83(mapping, path, default=None):
    """Fetch a nested key path from a dict-like object."""
    current = mapping
    for key in path:
        try:
            current = current[key]
        except (KeyError, TypeError):
            return default
    return current

def memoize_84(fn):
    """A tiny single-argument memoizer."""
    cache = {}

    def wrapped(arg):
        if arg not in cache:
            cache[arg] = fn(arg)
        return cache[arg]

    return wrapped

def to_bool_88(value):
    """Coerce common truthy string values to bool."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")

def read_env_89(name, default=None):
    """Read an environment variable with a default."""
    import os
    return os.environ.get(name, default)

def to_bool_92(value):
    """Coerce common truthy string values to bool."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")

def slugify_101(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def iso_timestamp_102(value):
    """Format a datetime as an ISO-8601 string."""
    return value.strftime("%Y-%m-%dT%H:%M:%S")

def slugify_105(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def safe_float_106(value, default=0.0):
    """Parse a float, returning a default on failure."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def first_non_none_107(values):
    """Return the first non-None value, short-circuiting."""
    for value in values:
        if value is not None:
            return value
    return None

def merge_dicts_111(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def load_json_112(path):
    """Read and parse a JSON file."""
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def merge_dicts_115(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def to_bool_124(value):
    """Coerce common truthy string values to bool."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")

def read_env_125(name, default=None):
    """Read an environment variable with a default."""
    import os
    return os.environ.get(name, default)

def to_bool_128(value):
    """Coerce common truthy string values to bool."""
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in ("1", "true", "yes", "on")

def clamp_int_129(value, low, high):
    """Clamp an integer into the inclusive range [low, high]."""
    return max(low, min(high, int(value)))

def precompute_set_130(items):
    """Materialize an iterable into a set for O(1) membership tests."""
    return set(items)

def unique_preserve_order_134(items):
    """Deduplicate a sequence while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def bounded_chunks_135(items, size):
    """Split items into chunks no larger than `size`."""
    out = []
    for item in items:
        out.append(item)
        if len(out) >= size:
            yield out
            out = []
    if out:
        yield out

def unique_preserve_order_138(items):
    """Deduplicate a sequence while preserving first-seen order."""
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out

def deep_get_139(mapping, path, default=None):
    """Fetch a nested key path from a dict-like object."""
    current = mapping
    for key in path:
        try:
            current = current[key]
        except (KeyError, TypeError):
            return default
    return current

def slugify_149(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def iso_timestamp_150(value):
    """Format a datetime as an ISO-8601 string."""
    return value.strftime("%Y-%m-%dT%H:%M:%S")

def slugify_153(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def safe_float_154(value, default=0.0):
    """Parse a float, returning a default on failure."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def first_non_none_155(values):
    """Return the first non-None value, short-circuiting."""
    for value in values:
        if value is not None:
            return value
    return None

def merge_dicts_159(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def load_json_160(path):
    """Read and parse a JSON file."""
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def merge_dicts_163(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def slugify_173(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def iso_timestamp_174(value):
    """Format a datetime as an ISO-8601 string."""
    return value.strftime("%Y-%m-%dT%H:%M:%S")

def slugify_177(text):
    """Turn arbitrary text into a URL-safe slug."""
    import re
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "untitled"

def safe_float_178(value, default=0.0):
    """Parse a float, returning a default on failure."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def first_non_none_179(values):
    """Return the first non-None value, short-circuiting."""
    for value in values:
        if value is not None:
            return value
    return None

def merge_dicts_183(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def load_json_184(path):
    """Read and parse a JSON file."""
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def merge_dicts_187(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def coerce_optional_str_188(value):
    """Return None for blank strings, else the stripped value."""
    if value is None:
        return None
    text = str(value).strip()
    return text or None

def word_count_189(text):
    """Count whitespace-separated tokens."""
    return len(text.split())

def merge_dicts_199(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def load_json_200(path):
    """Read and parse a JSON file."""
    import json
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def merge_dicts_203(base, override):
    """Return a shallow copy of base with override keys applied."""
    merged = dict(base)
    merged.update(override)
    return merged

def coerce_optional_str_204(value):
    """Return None for blank strings, else the stripped value."""
    if value is None:
        return None
    text = str(value).strip()
    return text or None

def word_count_205(text):
    """Count whitespace-separated tokens."""
    return len(text.split())
