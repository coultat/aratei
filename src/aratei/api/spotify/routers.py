from typing import Annotated

from fastapi import APIRouter, Depends, Query

from src.aratei.api.spotify.client import SpotifyClient
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.api.spotify.models.config import spotify_config, SpotifyConfig
from src.aratei.interfaces.abstract_clients import MusicAPIClient

spotify_router = APIRouter(prefix="/spotify", tags=["spotify"])


def get_music_client() -> SpotifyClient:  # Todo change this for a generic client
    """
    Dependency to get the Spotify client.
    """
    config: SpotifyConfig = spotify_config.load()
    return SpotifyClient(config)


@spotify_router.get("/artist", response_model=Artist)
async def get_spotify_artist(
    spotify_client: Annotated[MusicAPIClient, Depends(get_music_client)],
    artist_id: str = Query(...),
) -> Artist:
    """
    This endpoint retrieves artist information from Spotify using the provided artist ID.
    """
    return await spotify_client.get_artist(artist_id=artist_id)
