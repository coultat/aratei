import httpx
import base64
from typing import Any
from functools import wraps
from datetime import datetime
from src.aratei.api.spotify.models.config import SpotifyConfig
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.api.spotify.models.requests import (
    HeadersData,
    SpotifyEndpoint,
)
from src.aratei.interfaces.abstract_clients import MusicAPIClient


class SpotifyClient(MusicAPIClient):
    def __init__(self, spotify_config: SpotifyConfig):
        self._spotify_config = spotify_config

    def wrap_token(func: Any):
        @wraps(func)
        async def _refresh_token(self, *args, **kwargs):
            if (
                not hasattr(self, "headers")
                or not hasattr(self, "_cached_token")
                or self.expires_in > datetime.now()
            ):
                await self.get_token()
            return await func(self, *args, **kwargs)

        return _refresh_token

    async def get_token(self) -> None:
        credentials = self._spotify_config.credentials
        credentials_b64 = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        try:
            async with httpx.AsyncClient(
                timeout=self._spotify_config.timeout,
                headers={"Authorization": f"Basic {credentials_b64}"},
            ) as client:
                response = await client.post(
                    url=self._spotify_config.auth_url,
                    data={"grant_type": HeadersData.CLIENT_CREDENTIALS},
                )
                response.raise_for_status()
                self.expires_in = response.json()["expires_in"]
                self._cached_token = True
                authorization = response.json()["access_token"]
                self.headers = {"Authorization": f"Bearer {authorization}"}

        except httpx.HTTPStatusError as err:
            raise Exception(f"Failed to retrieve token: {err} - {response.text}")

        except httpx.TimeoutException as err:
            raise Exception(f"Connection Time out: {err=}")

    @wrap_token
    async def get_artist(self, artist_id: str) -> Artist:
        try:
            async with httpx.AsyncClient(
                base_url=self._spotify_config.base_url,
                timeout=self._spotify_config.timeout,
            ) as client:
                response = await client.get(
                    url=SpotifyEndpoint.ARTIST + artist_id, headers=self.headers
                )
                response.raise_for_status()
                return Artist.model_validate(response.json())

        except httpx.HTTPStatusError as err:
            raise Exception(f"Artist not found {err=}")
        except httpx.TimeoutException as err:
            raise Exception(f"Connection Timed out: {err=}")
