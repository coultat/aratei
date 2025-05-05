from pydantic import Field
from pydantic_settings import SettingsConfigDict
from pathlib import Path
from typing import ClassVar, Self
from pydantic_settings import BaseSettings


env_file = Path(__file__).parent.parent.parent.parent.parent.parent / "default.env"


class InternalCachedBaseSettings(BaseSettings):
    """Base class for settings with caching without vault access. Exists to prevent circular imports."""

    _cached_instance: ClassVar[Self | None] = None

    @classmethod
    def load(cls) -> BaseSettings:
        """Get settings from the usual places - env, secret files. Caches the result indefinitely."""
        # can't use cache decorator because of typing issues so we create our own cache
        if cls._cached_instance is None:
            cls._cached_instance = cls()
        return cls._cached_instance


class SpotifyConfig(InternalCachedBaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )
    client_id: str = Field(..., validation_alias="SPOTIFY_CLIENT_ID")
    client_secret: str = Field(..., validation_alias="SPOTIFY_CLIENT_SECRET")
    auth_url: str = Field(..., validation_alias="SPOTIFY_AUTH_URL")
    timeout: int = Field(..., validation_alias="SPOTIFY_TIMEOUT")
    base_url: str = Field(..., validation_alias="SPOTIFY_BASE_URL")

    @property
    def credentials(self):
        return f"{self.client_id}:{self.client_secret}"


spotify_config = SpotifyConfig.load()
