from src.tests.integration.conftest import session
from src.aratei.api.spotify.models.artists import Artist
from src.aratei.db.repositories.artist_repository import add_artist, get_artist
from src.aratei.db.mappers.artist_mapper import mapp_artist_db


def test_add_artist_no_duplicates(session, raw_artist):
    """
    Test that adding an existing artist does not create duplicates in the database.
    """
    # Given the artist, the session and the expected result
    artist = raw_artist
    artist = Artist.model_validate(artist)

    # When mapping the artist model and storing it in the db
    artist_db = mapp_artist_db(artist)
    add_artist(artist_db, session)

    # And fetching the artist from the db
    result = get_artist(artist.artist_id, session)

    # Then the result should match the expected values
    assert result.artist_id == artist.artist_id
    assert result.name == artist.name

    # Now try to add the same artist again
    add_artist(artist_db, session)

    # Fetch the artist again
    result_after_second_add = get_artist(artist.artist_id, session)

    # Ensure the artist is still the same, and no duplicates exist
    assert result_after_second_add.artist_id == artist.artist_id
    assert result_after_second_add.name == artist.name
