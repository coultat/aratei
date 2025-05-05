from pydantic import BaseModel, Field, HttpUrl, RootModel, ConfigDict


class ExternalURLs(BaseModel):
    spotify: HttpUrl = Field(alias="spotify", description="Spotify URL")


class Followers(BaseModel):
    href: HttpUrl | None = Field(alias="href", description="Followers HREF")
    total: int = Field(alias="total", description="Total number of followers")


class Genres(RootModel):
    root: list[str]


class ArtistImage(BaseModel):
    height: int = Field(alias="height", description="Image height")
    width: int = Field(alias="width", description="Image width")
    url: HttpUrl = Field(alias="url", description="Image URL")


class Artist(BaseModel):
    external_urls: ExternalURLs = Field(
        alias="external_urls", description="External URLs"
    )
    followers: Followers
    genres: Genres | None = Field(default=None, alias="genres", description="Genres")
    href: HttpUrl = Field(alias="href", description="Artist URL")
    artist_id: str = Field(alias="id", description="Artist ID")
    images: list[ArtistImage]
    name: str = Field(alias="name", description="Artist name")
    popularity: int = Field(alias="popularity", description="Artist popularity")
    type: str = Field(alias="type", description="Type of artist")
    uri: str = Field(alias="uri", description="Artist URI")
