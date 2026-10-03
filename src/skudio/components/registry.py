"""Component registry: maps qualname (metadata, Python class)."""

from __future__ import annotations

import importlib

from skudio.components.metadata import ComponentMetadata
from skudio.core.errors import RegistryError


class Registry:
    """In-memory registry of components discoverable by the UI and compiler."""

    def __init__(self) -> None:
        """Create an empty registry."""
        self._entries: dict[str, ComponentMetadata] = {}
        self._class_cache: dict[str, type] = {}

    def register(self, meta: ComponentMetadata) -> None:
        """Add 'meta' to the registry. Raises if the qualname is a duplicate."""
        if meta.qualname in self._entries:
            raise RegistryError("Component already registered",
                context={"qualname": meta.qualname},)

        self._entries[meta.qualname] = meta

    def register_many(self, metas: list[ComponentMetadata]) -> None:
        """Register every metadata entry in 'metas'."""
        for m in metas:
            self.register(m)

    def get(self, qualname: str) -> ComponentMetadata:
        """Return the metadata for 'qualname'. Raises on unknown qualnames."""
        try:
            return self._entries[qualname]
        except KeyError:
            raise RegistryError("Unknown component", context={"qualname": qualname}) from None

    def list(self) -> list[ComponentMetadata]:
        """Return every registered component's metadata."""
        return list(self._entries.values())

    def resolve_class(self, qualname: str) -> type:
        """Import and return the Python class for the given qualname.

        Rejects any qualname not present in the registry. The IR is
        user-authored data; without this check, a crafted graph could
        drive `importlib.import_module` at any qualname the interpreter
        can reach and then instantiate the resulting class.
        """
        if qualname not in self._entries:
            raise RegistryError("Qualname not registered; refusing to import",
                context={"qualname": qualname},)

        cached = self._class_cache.get(qualname)
        if cached is not None:
            return cached

        module_name, _, cls_name = qualname.rpartition(".")
        if not module_name:
            raise RegistryError("Qualname must be fully qualified",
                context={"qualname": qualname})

        try:
            module = importlib.import_module(module_name)
            cls = getattr(module, cls_name)
        except (ImportError, AttributeError) as exc:
            raise RegistryError("Cannot import component",
                context={"qualname": qualname, "error": str(exc)},
            ) from exc

        self._class_cache[qualname] = cls
        return cls


# mutable singleton, not a constant
# pylint: disable=invalid-name
_default_registry: Registry | None = None


def default_registry() -> Registry:
    """Return the process-global registry, initialised on first call."""
    # pylint: disable=import-outside-toplevel
    # pylint: disable=global-statement
    global _default_registry

    if _default_registry is None:
        _default_registry = Registry()

        # Providers registered here on first access to avoid import cycles.
        from skudio.components.providers.sklearn.register import register_sklearn_components
        register_sklearn_components(_default_registry)
    return _default_registry


def reset_default_registry() -> None:
    """Test hook."""
    # pylint: disable=global-statement
    global _default_registry
    _default_registry = None


__all__: list[str] = ["Registry", "default_registry", "reset_default_registry"]
