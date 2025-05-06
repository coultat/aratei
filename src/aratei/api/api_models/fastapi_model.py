from src.aratei.api.api_models.base_settings import InternalCachedBaseSettings


class AppConfig(InternalCachedBaseSettings):
    """
    App config for aratei. Can be used as a standalone config or as part of another config.
    General settings of the application belong here.
    """

    name: str = "aratei"
    version: str = "1.0.0"
