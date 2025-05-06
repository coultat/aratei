from src.aratei.api.api_models.fastapi_model import AppConfig
from src.aratei.api.spotify.routers import spotify_router
from src.aratei.api.app.fastapi_config import create_fastapi_app

fastapi_app = create_fastapi_app(app_config=AppConfig.load(), version="0.1.0")

fastapi_app.include_router(spotify_router)


@fastapi_app.get("/")
async def hello_world():
    return {"message": "Hello World"}
