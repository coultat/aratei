import pytest


@pytest.fixture
def mock_spotify_client_dict():
    return {
        "access_token": "mock_access_token",
        "token_type": "mock_token_type",
        "expires_in": 3600,
    }


@pytest.fixture
def mock_spotify_artist():
    return {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/2ziB7fzrXBoh1HUPS6sVFn"
        },
        "followers": {"href": None, "total": 4905201},
        "genres": ["grunge", "post-grunge", "alternative metal"],
        "href": "https://api.spotify.com/v1/artists/2ziB7fzrXBoh1HUPS6sVFn",
        "id": "2ziB7fzrXBoh1HUPS6sVFn",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb5a865295befda9e060a72cb0",
                "width": 640,
            },
            {
                "height": 320,
                "url": "https://i.scdn.co/image/ab676161000051745a865295befda9e060a72cb0",
                "width": 320,
            },
            {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f1785a865295befda9e060a72cb0",
                "width": 160,
            },
        ],
        "name": "Audioslave",
        "popularity": 73,
        "type": "artist",
        "uri": "spotify:artist:2ziB7fzrXBoh1HUPS6sVFn",
    }
