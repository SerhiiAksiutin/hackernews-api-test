"""Shared pytest fixtures for Hacker News API tests."""

import os
import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    """Get base URL for Hacker News API from environment or use default."""
    return os.getenv(
        "HB_BASE_URL",
        "https://hacker-news.firebaseio.com/v0"
    )


@pytest.fixture(scope="session")
def http_session():
    """Create a shared HTTP session with timeout configuration."""
    session = requests.Session()
    session.timeout = 5
    return session

