from fastapi import APIRouter, Depends, Query

from src.aratei.api.spotify.client import SpotifyClient
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.api.spotify.models.config import spotify_config, SpotifyConfig
from src.aratei.db.session import session
from src.aratei.db.models.artist import ArtistDB
from src.aratei.services.artist_services import fetch_and_store_artist


spotify_router = APIRouter(prefix="/spotify", tags=["spotify"])


def get_spotify_client() -> SpotifyClient:
    """
    Dependency to get the Spotify client.
    """
    config: SpotifyConfig = spotify_config.load()
    return SpotifyClient(config)


@spotify_router.get("/artist", response_model=Artist)
async def import_artist(
    artist_id: str = Query(...),
    spotify_client: SpotifyClient = Depends(get_spotify_client),
) -> Artist:
    """
    This endpoint retrieves artist information from Spotify using the provided artist ID.
    """
    return await fetch_and_store_artist(artist_id, spotify_client)
