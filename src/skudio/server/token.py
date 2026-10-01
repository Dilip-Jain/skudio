"""One-time URL token for guarding."""

from __future__ import annotations

import hmac
import secrets

_TOKEN_BYTES = 32

def new_token() -> str:
    """Return a fresh URL-safe token."""
    return secrets.token_urlsafe(_TOKEN_BYTES)

def verify_token(expected: str, candidate: str) -> bool:
    """Verify token."""
    return hmac.compare_digest(expected.encode("utf-8"), candidate.encode("utf-8"))
