"""Turn a probe mapping into something a person can read.

Pure functions only - no I/O, no subprocesses. Nothing in this module should
need to change when the probes are hardened.
"""

from __future__ import annotations

LABELS = {
    "kernel": "Kernel",
    "host": "Host",
    "user": "User",
}


def render(values: dict[str, str]) -> str:
    """Render the report as aligned `Label: value` lines, in a stable order."""
    known = [key for key in LABELS if key in values]
    extra = sorted(key for key in values if key not in LABELS)
    keys = known + extra
    if not keys:
        return "no data collected"
    width = max(len(LABELS.get(key, key)) for key in keys)
    return "\n".join(f"{LABELS.get(key, key):<{width}} : {values[key]}" for key in keys)
