from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from src.aratei.api.api_models.fastapi_model import AppConfig
from starlette.responses import Response


def create_fastapi_app(app_config: AppConfig.load(), version: str) -> FastAPI:
    """
    Create fastapi app from appconfig and version.
    Also sets an exception handler and adds a redirect from / to /docs.
    lifespan can be used to run tasks before and after the app starts and stops respectively, like migrations.

    """

    app = FastAPI(
        title=app_config.name,
        version=version,
        description=f"API for {app_config.name} - API version: 1 - app version: {version}",
    )
    app.exception_handler(RequestValidationError)(request_validation_exception_handler)

    app.get("/")(lambda: Response("/docs"))
    return app
