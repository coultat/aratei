from src.aratei.api.spotify.models.artists import Artist
from src.aratei.api.spotify.client import SpotifyClient
from src.aratei.db.mappers.artist_mapper import mapp_artist_db
from src.aratei.db.repositories.artist_repository import add_artist
from src.aratei.db.session import session


async def fetch_and_store_artist(artist_id: str, spotify_client: SpotifyClient) -> Artist:
    artist = await spotify_client.get_artist(artist_id=artist_id)
    artist_db = mapp_artist_db(artist)
    add_artist(artist_db, session)
    return artist