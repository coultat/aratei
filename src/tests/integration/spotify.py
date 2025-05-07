from src.tests.integration.conftest import test_client
import pytest
from unittest.mock import patch
from src.aratei.api.spotify.models.artists import Artist


def test_hello_world():
    response = test_client.get("/hello_world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
@patch("httpx.post")
@patch("httpx.get")
def test_get_artist(mock_get_artist, mock_artist): #, mock_token, mock_artist):
    # Given the mock token and artist data
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
