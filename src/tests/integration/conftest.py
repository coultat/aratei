from fastapi.testclient import TestClient
from pytest_httpx import HTTPXMock
from src.aratei.api.app.app import fastapi_app
import httpx
import pytest
import json

test_client = TestClient(fastapi_app)


@pytest.fixture
def mock_get_token(httpx_mock: HTTPXMock) -> HTTPXMock:
    httpx_mock.add_response(
        url="https://api.spotify.com/v1/token",
        json={
            "access_token": "mock_access_token",
            "token_type": "Bearer",
            "expires_in": 3600,
        },
    )
    return httpx_mock


@pytest.fixture
def mock_token():
    token = {
        "access_token": "mock_access_token",
        "token_type": "Bearer",
        "expires_in": 3600,
    }

    return httpx.Response(
        status_code=200,
        content=json.dumps(token).encode("utf-8"),
        request=httpx.Request(
            method="POST",
            url="https://accounts.spotify.com/api/token",
            headers={"Authorization": "Basic lolailo"},
        ),
    )


@pytest.fixture
def mock_artist():
    artist = {
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

    return httpx.Response(
        status_code=200,
        content=json.dumps(artist).encode("utf-8"),
        request=httpx.Request(
            method="GET",
            url="https://api.spotify.com/v1/artists",
            params={"artist_id": "2ziB7fzrXBoh1HUPS6sVFn"},
        ),
    )
