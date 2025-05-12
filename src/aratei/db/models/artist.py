from src.aratei.db.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class ArtistDB(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    name = Column("artist_name", String)
    artist_id = Column("artist_id", String)
    popularity = Column("popularity", Integer)
    type = Column("type", String)
    uri = Column("uri", String)
    href = Column("href", String)

    followers = relationship("FollowersDB", uselist=False, back_populates="artist")
    images = relationship("ImagesDB", back_populates="artist")

    def __init__(self, name, artist_id, popularity, type, uri, href, images, followers):
        self.name = name
        self.artist_id = artist_id
        self.popularity = popularity
        self.type = type
        self.uri = uri
        self.href = href
        self.images = images
        self.followers = followers

    def __repr__(self):
        return f"<Artist(name={self.name}, artist_id={self.artist_id}>"


class ImagesDB(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    height = Column("height", Integer)
    width = Column("width", Integer)
    url = Column("url", String)

    artist_id = Column(String, ForeignKey("artists.artist_id"))
    artist = relationship("ArtistDB", back_populates="images")


class FollowersDB(Base):
    __tablename__ = "followers"

    id = Column(Integer, primary_key=True)
    href = Column("href", String)
    total = Column("total", Integer)

    artist_id = Column(Integer, ForeignKey("artists.artist_id"))
    artist = relationship("ArtistDB", back_populates="followers")
