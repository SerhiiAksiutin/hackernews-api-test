"""Tests for the Hacker News items endpoint."""

import pytest


@pytest.fixture(scope="module")
def get_topstories(base_url, http_session):
    """Get list of top story IDs."""
    url = f"{base_url}/topstories.json"
    response = http_session.get(url)
    return response.json()


def test_current_top_story_returns_200(base_url, http_session, get_topstories):
    """Test that top story endpoint returns 200 status code."""
    url = f"{base_url}/item/{get_topstories[0]}.json"
    response = http_session.get(url)
    assert response.status_code == 200


def test_current_top_story_returns_json(base_url, http_session, get_topstories):
    """Test that top story endpoint returns JSON content type."""
    url = f"{base_url}/item/{get_topstories[0]}.json"
    response = http_session.get(url)
    assert "application/json" in response.headers.get("Content-Type", "")


def test_current_top_story_returns_required_fields(base_url, http_session, get_topstories):
    """Test that top story has required fields."""
    url = f"{base_url}/item/{get_topstories[0]}.json"
    response = http_session.get(url)
    data = response.json()
    required_fields = ["id", "time", "type", "title", "by"]
    
    # NOTE: Only id is marked as required in API docs. TODO: Follow up
    assert all(data.get(field) for field in required_fields), "Required field(s) missing."
    
    # Validate field types
    assert all(isinstance(data[field], str) for field in required_fields[2:])
    assert all(isinstance(data[field], int) for field in required_fields[:2])


def test_current_top_story_returns_valid_id(base_url, http_session, get_topstories):
    """Test that top story ID matches requested ID."""
    url = f"{base_url}/item/{get_topstories[0]}.json"
    response = http_session.get(url)
    data = response.json()
    assert data.get("id") == get_topstories[0]
    assert isinstance(data["id"], int)


def test_current_top_story_returns_valid_type(base_url, http_session, get_topstories):
    """Test that top story type is 'story'."""
    url = f"{base_url}/item/{get_topstories[0]}.json"
    response = http_session.get(url)
    assert response.json().get("type") == "story"


def test_invalid_story_id(base_url, http_session):
    """Test that invalid story ID returns None."""
    url = f"{base_url}/item/invalid_id.json"
    response = http_session.get(url)
    assert response.json() is None


@pytest.fixture(scope="module")
def get_top_comment_id(base_url, http_session, get_topstories):
    """Get a comment ID from a story with comments."""
    for story_id in get_topstories[:30]:
        url = f"{base_url}/item/{story_id}.json"
        response = http_session.get(url)
        data = response.json()

        if data.get("kids"):
            return data["kids"][0]
    
    pytest.fail("First 30 top stories are missing comments.")


def test_comment_found(base_url, http_session, get_top_comment_id):
    """Test that comment endpoint returns valid comment data."""
    url = f"{base_url}/item/{get_top_comment_id}.json"
    response = http_session.get(url)
    data = response.json()
    assert data.get("id") == get_top_comment_id
    assert data.get("type") == "comment"


def test_missing_item_id(base_url, http_session):
    """Test that missing item id returns 401."""
    missing_id = ""
    url = f"{base_url}/item/{missing_id}.json"
    response = http_session.get(url)
    assert response.status_code == 401
    assert response.json().get("error") == "Permission denied"

