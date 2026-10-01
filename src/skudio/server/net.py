"""Loopback binding + free-port selection for the local dev server."""

from __future__ import annotations

import socket

LOOPBACK = "127.0.0.1"

def pick_free_port() -> int:
    """Request OS for a free port on the loopback interface."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((LOOPBACK, 0))
        return s.getsockname()[1]

def ensure_loopback(host: str) -> str:
    """Ensure loopback host (Localhost-only)"""
    if host not in {LOOPBACK, "localhost", "::1"}:
        raise ValueError(f"refusing to bind to non-loopback host {host!r}; use {LOOPBACK!r}")
    return host
