from pydantic import Field
from pydantic_settings import SettingsConfigDict
from src.aratei.config.settings import env_file
from src.aratei.api.api_models.base_settings import InternalCachedBaseSettings


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
