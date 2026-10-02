"""Component and dataset references."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict


Role = Literal["numeric", "categorical", "datetime", "text", "unknown"]

class ComponentRef(BaseModel):
    """Reference to a registered component (estimator, transformer, composite)."""
    model_config = ConfigDict(extra="forbid")

    provider: str
    qualname: str
    version: str = ""


class ColumnSchema(BaseModel):
    """Schema of a single dataset column."""
    model_config = ConfigDict(extra="forbid")

    name: str
    dtype: str
    role: Role = "unknown"


class DatasetSchema(BaseModel):
    """Schema of a dataset: ordered list of column descriptors."""
    model_config = ConfigDict(extra="forbid")

    columns: list[ColumnSchema] = []

    def names(self) -> list[str]:
        """Return the column names in declaration order."""
        return [c.name for c in self.columns]


class DatasetRef(BaseModel):
    """Locates a dataset persisted under a project directory."""
    model_config = ConfigDict(extra="forbid")

    id: str
    kind: Literal["csv", "parquet"]
    path: str
    schema_: DatasetSchema = DatasetSchema()
