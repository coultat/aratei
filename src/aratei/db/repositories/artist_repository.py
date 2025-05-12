from src.aratei.db.models.artist import ArtistDB
from sqlalchemy.orm import Session
from sqlalchemy import Column
from src.aratei.api.spotify.models.artists import Artist


def _add_artist(artist: ArtistDB, db: Session) -> None:
    """
    Add an artist to the database.
    """
    db.add(artist)
    db.commit()
    db.refresh(artist)


def add_artist(artist: ArtistDB, db: Session) -> None:
    if get_artist(artist.artist_id, db) is None:
        _add_artist(artist, db)


def get_artist(artist_id: Column[str], db: Session):
    result = db.query(ArtistDB).filter(ArtistDB.artist_id == artist_id).first()
    return result


def get_artist_by_name(name: str, db: Session):
    result = db.query(ArtistDB).filter(ArtistDB.name == name).first()
    result = Artist.model_validate(result)
    return result
