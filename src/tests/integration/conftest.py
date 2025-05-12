from fastapi.testclient import TestClient
from pytest_httpx import HTTPXMock
from src.aratei.api.app.app import fastapi_app
import httpx
import json
import pytest
from sqlalchemy import create_engine
from src.aratei.db.models.base import Base
from sqlalchemy.orm import sessionmaker

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
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture
def session(in_memory_db):
    Session = sessionmaker(bind=in_memory_db)
    session = Session()
    yield session
    session.rollback()
    session.close()


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


@pytest.fixture
def raw_artist():
    return {
  "external_urls": {
    "spotify": "https://open.spotify.com/artist/6GbCJZrI318Ybm8mY36Of5"
  },
  "followers": {
    "href": None,
    "total": 1909810
  },
  "genres": [
    "funk rock",
    "alternative metal",
    "rap metal",
    "grunge"
  ],
  "href": "https://api.spotify.com/v1/artists/6GbCJZrI318Ybm8mY36Of5",
  "id": "6GbCJZrI318Ybm8mY36Of5",
  "images": [
    {
      "height": 1000,
      "width": 1000,
      "url": "https://i.scdn.co/image/765ad08f23f828d1a850c47ac417d7be260af932"
    },
    {
      "height": 640,
      "width": 640,
      "url": "https://i.scdn.co/image/85715abdbcc9f1326915a891360d8cedb09d9379"
    },
    {
      "height": 200,
      "width": 200,
      "url": "https://i.scdn.co/image/4f3551a1b2cf8b1ea1d026a80d718044a6f6f817"
    },
    {
      "height": 64,
      "width": 64,
      "url": "https://i.scdn.co/image/87848b2d4dc66640f83601753f355a1eceb1b4ee"
    }
  ],
  "name": "Faith No More",
  "popularity": 63,
  "type": "artist",
  "uri": "spotify:artist:6GbCJZrI318Ybm8mY36Of5"
}