from pydantic import BaseModel


class AppConfig(BaseModel):
    """
    App config for aratei. Can be used as a standalone config or as part of another config.
    General settings of the application belong here.
    """

    name: str = "aratei"
    version: str = "1.0.0"
