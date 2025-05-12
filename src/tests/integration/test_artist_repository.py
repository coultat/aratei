from src.tests.integration.conftest import session
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.db.repositories.artist_repository import add_artist, get_artist
from src.aratei.db.mappers.artist_mapper import mapp_artist_db


def test_add_artist(session, raw_artist):
    """
    Test that the add_artist function correctly maps an Artist
    model to an ArtistDB model and stores it in the database.
    """
    # Given the artist, the session and the expected result
    artist = raw_artist
    artist = Artist.model_validate(artist)
    expected_artist_name = "Faith No More"

    # When mapping the artist model and storing it in the db
    artist_db = mapp_artist_db(artist)
    add_artist(artist_db, session)

    # And fetching the artist from the db
    result = get_artist(artist.artist_id, session)

    # Then the result should match the expected values
    assert result.artist_id == artist.artist_id
    assert result.name == artist.name








