"""Canonical JSON serialization for IR graphs."""

from __future__ import annotations

import json
from typing import Any

from skudio.core.ir.graph import Graph


def canonical_dict(graph: Graph) -> dict[str, Any]:
    """Return the graph as a canonical dict (sorted keys, defaults included)"""
    data = graph.model_dump(mode="json")
    return data

def canonical_json(graph: Graph) -> str:
    """Return canonical, byte-stable JSON for a graph."""
    return json.dumps(
        canonical_dict(graph),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    )
