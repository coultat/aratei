from src.aratei.api.api_models.base_settings import InternalCachedBaseSettings
from pydantic_settings import SettingsConfigDict
from src.aratei.config.settings import env_file
from pydantic import Field


class AppConfig(InternalCachedBaseSettings):
    """
    App config for aratei. Can be used as a standalone config or as part of another config.
    General settings of the application belong here.
    """

    model_config = SettingsConfigDict(
        env_file=env_file,
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )
    name: str = Field(..., validation_alias="APP_NAME")
    version: str = Field(..., validation_alias="APP_VERSION")
    description: str = Field(..., validation_alias="APP_DESCRIPTION")
