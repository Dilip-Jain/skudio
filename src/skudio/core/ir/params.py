"""Parameter values on IR nodes: literal, reference, or search space."""

from __future__ import annotations

from typing import Annotated, Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class LiteralValue(BaseModel):
    """A JSON-scalar, list, or dict literal."""
    model_config = ConfigDict(extra="forbid")

    kind: Literal["literal"] = "literal"
    value: Any = None


class Reference(BaseModel):
    """A pointer to a dataset column or an upstream node port."""
    model_config = ConfigDict(extra="forbid")

    kind: Literal["reference"] = "reference"
    ref: str


class ChoiceSpace(BaseModel):
    """Search space: pick one of an explicit list."""
    model_config = ConfigDict(extra="forbid")

    kind: Literal["choice"] = "choice"
    choices: list[Any]


class RangeSpace(BaseModel):
    """Seach space: bounded interval, optionally stepped or log-scaled."""
    model_config = ConfigDict(extra="forbid")

    kind: Literal["range"] = "range"
    low: float
    high: float
    step: float | None = None
    log: bool = False

    @model_validator(mode="after")
    def _bounds(self) -> RangeSpace:
        if self.low > self.high:
            raise ValueError("Low must be <= High")
        return self


class DistributionSpace(BaseModel):
    """Seach space: namedd continuous distribution over `[low, high]`."""
    model_config = ConfigDict(extra="forbid")

    kind: Literal["distribution"] = "distribution"
    dist: Literal["uniform", "loguniform", "randint"]
    low: float
    high: float


_SpaceUnion = Annotated[
    ChoiceSpace | RangeSpace | DistributionSpace,
    Field(discriminator="kind"),
]


class SearchSpace(BaseModel):
    """A hyperparameter search space, legal only under a `search` scope."""
    model_config = ConfigDict(extra="forbid")

    kind: Literal["search_space"] = "search_space"
    space: _SpaceUnion


ParamValue = Annotated[
    LiteralValue | Reference | SearchSpace,
    Field(discriminator="kind"),
]

