from src.aratei.api.spotify.models.requests import SpotifyRequests
from src.aratei.api.spotify.models.artists import Artist


def test_spotify_client(mock_spotify_client_dict):
    # Given the mock data
    mock_data = mock_spotify_client_dict

    # When the SpotifyRequests model is created
    spotify_requests = SpotifyRequests(**mock_data)

    # Then the model should be created successfully
    assert spotify_requests.access_token == mock_data["access_token"]
    assert spotify_requests.token_type == mock_data["token_type"]
    assert spotify_requests.expires_in == mock_data["expires_in"]


def test_spotify_artist(mock_spotify_artist):
    # Given the mock data
    mock_artist = mock_spotify_artist

    # When the SpotifyArtist model is created
    spotify_requests = Artist(**mock_artist)

    # Then the model should be created successfully
    assert spotify_requests.name == mock_artist["name"]
    assert spotify_requests.artist_id == mock_artist["id"]
    assert spotify_requests.uri == mock_artist["uri"]
