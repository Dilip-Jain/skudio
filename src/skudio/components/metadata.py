"""Component metadata"""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

WidgetHint = Literal["number", "int", "slider", "select", "toggle", "text", "columns"]
Category = Literal["preprocessing", "estimator", "composite", "search"]

# TODO: Add support "clustering"
Task = Literal["classification", "regression"] #, "clustering"]


class ParamDescriptor(BaseModel):
    """Widget-hint metadata for one parameter of a component."""
    model_config = ConfigDict(extra="forbid")

    name: str
    default: Any = None
    widget: WidgetHint = "text"
    choices: list[Any] | None = None
    min: float | None = None
    max: float | None = None
    step: float | None = None
    tier: Literal["basic", "advanced"] = "basic"
    description: str = ""


class ComponentMetadata(BaseModel):
    """Registry entry for one sklearn component (estimator / transformer / composite)."""
    model_config = ConfigDict(extra="forbid")

    qualname: str
    display_name: str
    category: Category
    task: Task | None = None
    version: str = ""
    description: str = ""
    doc_url: str = ""
    params: list[ParamDescriptor] = []
