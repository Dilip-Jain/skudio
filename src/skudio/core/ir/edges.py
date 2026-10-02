"""Edges between IR node ports."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class NodeRef(BaseModel):
    """Reference to a specific port on a specific node."""
    model_config = ConfigDict(extra="forbid")

    node_id: str
    port: str


class Edge(BaseModel):
    """A directed edge from one node's output port to another node's input port."""
    model_config = ConfigDict(extra="forbid")

    src: NodeRef
    dst: NodeRef
