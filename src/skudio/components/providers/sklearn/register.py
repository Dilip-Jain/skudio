"""Register the sklearn provider with a given Registry."""

from __future__ import annotations

from skudio.components.providers.sklearn.manifest import ALL_COMPONENTS
from skudio.components.registry import Registry


def register_sklearn_components(registry: Registry) -> None:
    """Register the curated sklearn manifest into `registry`, stamping the version."""
    version = _sklearn_version()
    for meta in ALL_COMPONENTS:
        stamped = meta if meta.version else meta.model_copy(update={"version": version})
        registry.register(stamped)


def _sklearn_version() -> str:
    try:
        # pylint: disable=import-outside-toplevel
        import sklearn
    except ImportError:
        return ""
    return getattr(sklearn, "__version__", "")
