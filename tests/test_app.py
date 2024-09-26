import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_search_tweets(client):
    # Test valid search term
    response = client.get("/api/search?term=music")
    assert response.status_code == 200
    data = response.get_json()
    assert "tweets_per_day" in data
    assert "unique_users" in data
    assert "avg_likes" in data
    assert "place_ids" in data
    assert "times_of_day" in data
    assert "most_active_user" in data


def test_no_search_term(client):
    # Test no search term
    response = client.get("/api/search")
    assert response.status_code == 400
    assert response.get_json()["error"] == "No search term provided"
