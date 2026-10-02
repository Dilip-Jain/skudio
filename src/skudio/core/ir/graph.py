"""Graph Root"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

from skudio.core.ir.edges import Edge
from skudio.core.ir.nodes import Node
from skudio.core.ir.refs import DatasetRef

IR_VERSION = "0.1"


class Graph(BaseModel):
    """A pipeline IR graph."""
    model_config = ConfigDict(extra="forbid")

    ir_version: Literal["0.1"] = IR_VERSION
    id: str
    name: str = ""
    nodes: list[Node] = []
    edges: list[Edge] = []
    dataset_ref: DatasetRef | None = None
    random_state: int | None = None
    metadata: dict[str, Any] = {}


# Node reference Graph via forward ref
Node.model_rebuild()
Graph.model_rebuild()
