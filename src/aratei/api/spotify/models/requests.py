from enum import EnumType

from pydantic import BaseModel, Field


class SpotifyRequests(BaseModel):
    access_token: str = Field(
        alias="access_token", description="Access token for Spotify API"
    )
    token_type: str = Field(
        alias="token_type", description="Token type for Spotify API"
    )
    expires_in: int = Field(
        alias="expires_in", description="Expiration time in seconds"
    )


class HeadersData(EnumType):
    CLIENT_CREDENTIALS = "client_credentials"


class SpotifyEndpoint(EnumType):
    ARTIST = "artists/"
    PLAYLIST = "playlists/"
