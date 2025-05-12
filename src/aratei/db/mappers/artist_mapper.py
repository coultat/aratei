from src.aratei.api.spotify.models.artists import Artist
from src.aratei.db.models.artist import ArtistDB, ImagesDB, FollowersDB


def _map_images(artist: Artist) -> list[ImagesDB]:
    """
    Convert the images from the artist to a list of ImagesDB.
    """
    images: list[ImagesDB] = []
    for image in artist.images:
        images.append(
            ImagesDB(width=image.width, height=image.height, url=str(image.url))
        )
    return images


def _map_followers(artist: Artist) -> FollowersDB:
    """
    Convert the followers from the artist to FollowersDB.
    """
    return FollowersDB(href=artist.followers.href, total=artist.followers.total)


def mapp_artist_db(artist: Artist) -> ArtistDB:
    images = _map_images(artist)
    followers = _map_followers(artist)

    return ArtistDB(
        name=artist.name,
        artist_id=artist.artist_id,
        popularity=artist.popularity,
        type=artist.type,
        uri=artist.uri,
        href=artist.href,
        images=images,
        followers=followers,
    )
