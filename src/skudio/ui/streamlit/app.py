"""skudio.ui.streamlit - Streamlit (Single-page, top-to-bottom flow) UI adapter for skudio."""

from __future__ import annotations

import os

import streamlit as st

import skudio
from skudio.server.token import verify_token


_TOKEN_ENV = "SKUDIO_TOKEN"


def main() -> None:
    """Streamlit entry point."""
    st.set_page_config(page_title=skudio.NAME, layout="wide")
    if not _token_ok():
        _lock_screen()
        return

    st.title(skudio.NAME)
    st.caption(skudio.TAGLINE)


def _token_ok() -> bool:
    """Check if the token is valid."""
    expected = os.environ.get(_TOKEN_ENV)
    if not expected:
        return True # dev-mode (--no-token or direct streamlit run)

    candidate = st.query_params.get("token", "")
    ok = verify_token(expected, candidate)
    if ok:
        st.session_state["_token_verified"] = True
    return ok or bool(st.session_state.get("_token_verified", False))


def _lock_screen() -> None:
    """Display a lock screen if the token is invalid."""
    st.title(skudio.NAME)
    st.error("Invalid token. Please provide a valid token in the URL query parameters.")
    st.stop()


# streamlit run app.py
if __name__ == "__main__":
    main()
