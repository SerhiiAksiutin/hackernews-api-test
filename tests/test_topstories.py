"""Tests for the Hacker News topstories endpoint."""


def test_topstories_returns_200(base_url, http_session):
    """Test that topstories endpoint returns 200 status code."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    assert response.status_code == 200


def test_topstories_returns_json(base_url, http_session):
    """Test that topstories endpoint returns JSON content type."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    assert "application/json" in response.headers.get("Content-Type", "")


def test_topstories_returns_list(base_url, http_session):
    """Test that topstories endpoint returns a list."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    assert isinstance(response.json(), list)


def test_topstories_returns_not_empty(base_url, http_session):
    """Test that topstories list is not empty."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    assert len(response.json()) > 0


def test_topstories_returns_int_list(base_url, http_session):
    """Test that topstories list contains only integers."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    assert all(isinstance(item, int) for item in response.json())


def test_topstories_returns_unique_ids(base_url, http_session):
    """Test that topstories list contains unique IDs."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    assert len(response.json()) == len(set(response.json()))

 