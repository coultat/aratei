from src.tests.integration.conftest import test_client
import pytest
from unittest.mock import patch
from src.tests.integration.conftest import session
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.db.repositories.artist_repository import add_artist, get_artist
from src.aratei.db.mappers.artist_mapper import mapp_artist_db


def test_hello_world():
    response = test_client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
@patch("httpx.post")
@patch("httpx.get")
def test_get_artist(mock_get_artist, mock_get_token, mock_token, mock_artist, session):
    # Given the mock token and artist data
    mock_get_token.return_value = mock_token
    mock_get_artist.return_value = mock_artist
    expected_artist_name = "Audioslave"

    # When calling the endpoint and the data is validated
    response = test_client.get(
        "/spotify/artist", params={"artist_id": "2ziB7fzrXBoh1HUPS6sVFn"}
    )
    artist = Artist.model_validate(response.json())


    # Then the response should match with the expected values
    assert response.status_code == 200
    assert artist.name == expected_artist_name


@pytest.mark.asyncio
@patch("httpx.post")
@patch("httpx.get")
def test_get_artist_invalid_id(mock_get_artist, mock_get_token, mock_token, session):
    # Given an invalid artist ID
    mock_get_token.return_value = mock_token
    mock_get_artist.return_value = None  # Simulate no artist found

    # When calling the endpoint with an invalid artist ID
    response = test_client.get(
        "/spotify/artist", params={"artist_id": "invalid_id"}
    )

    # Then the response should indicate an error
    assert response.status_code == 404
    assert "error" in response.json()  # Assuming the error response contains an "error" key


# Additional test to check for unauthorized access
@pytest.mark.asyncio
@patch("httpx.post")
@patch("httpx.get")
def test_get_artist_unauthorized(mock_get_artist, mock_get_token, session):
    # Given unauthorized access scenario
    mock_get_token.return_value = None  # Simulate no token available

    # When calling the endpoint without authorization
    response = test_client.get(
        "/spotify/artist", params={"artist_id": "2ziB7fzrXBoh1HUPS6sVFn"}
    )

    # Then the response should indicate unauthorized access
    assert response.status_code == 401
    assert "error" in response.json()