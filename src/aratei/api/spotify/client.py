import httpx
import base64

from src.aratei.api.spotify.models.config import SpotifyConfig
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.api.spotify.models.requests import (
    SpotifyRequests,
    HeadersData,
    SpotifyEndpoint,
)
from src.aratei.interfaces.abstract_clients import MusicAPIClient


class SpotifyClient(MusicAPIClient):
    def __init__(self, spotify_config: SpotifyConfig):
        self._spotify_config = spotify_config

    async def get_token(self) -> SpotifyRequests:
        credentials = self._spotify_config.credentials
        credentials_b64 = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        try:
            response = httpx.post(
                self._spotify_config.auth_url,
                headers={"Authorization": f"Basic {credentials_b64}"},
                data={"grant_type": HeadersData.CLIENT_CREDENTIALS},
                timeout=self._spotify_config.timeout,
            )
            response.raise_for_status()
            token_data = SpotifyRequests.model_validate(response.json())
            return token_data
        except httpx.HTTPStatusError as err:
            raise Exception(f"Failed to retrieve token: {err} - {response.text}")
        except httpx.TimeoutException as err:
            raise Exception(f"Connection Timedout: {err=}")

    async def get_artist(self, artist_id: str) -> Artist:
        try:
            token = await self.get_token()
            response = httpx.get(
                self._spotify_config.base_url + SpotifyEndpoint.ARTIST + artist_id,
                headers={"Authorization": f"{token.token_type} {token.access_token}"},
            )
            response.raise_for_status()
            return Artist.model_validate(response.json())

        except httpx.HTTPStatusError as err:
            raise Exception(f"Artist not found {err=}")
        except httpx.TimeoutException as err:
            raise Exception(f"Connection Timed out: {err=}")
