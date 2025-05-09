from src.aratei.db.models.artist import ArtistDB
from src.aratei.db.session import session


def _add_artist(artist: ArtistDB, db: session) -> None:
    """
    Add an artist to the database.
    """
    db.add(artist)
    db.commit()
    db.refresh(artist)


def add_artist(artist: ArtistDB, db: session) -> None:
    if get_artist(artist.artist_id, db) is None:
        _add_artist(artist, db)


def get_artist(artist_id: str, db: session):
    result = db.query(ArtistDB).filter(ArtistDB.artist_id == artist_id).first()
    return result

