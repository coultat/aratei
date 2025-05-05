from typing import Annotated
from fastapi import FastAPI, Depends

from src.aratei.api.spotify.client import SpotifyClient
from src.aratei.api.spotify.models.config import spotify_config, SpotifyConfig
from src.aratei.api.spotify.routers import spotify_router

fastapi_app = FastAPI()

fastapi_app.include_router(spotify_router)


@fastapi_app.get("/")
async def root():
    return {"message": "Hello World"}
