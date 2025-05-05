from src.aratei.api.spotify.routers import spotify_router
from fastapi import FastAPI

fastapi_app = FastAPI()

fastapi_app.include_router(spotify_router)


@fastapi_app.get("/")
async def root():
    return {"message": "Hello World"}
