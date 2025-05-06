from abc import ABC, abstractmethod


class MusicAPIClient(ABC):
    @abstractmethod
    def get_token(self):
        raise NotImplementedError("Method get_token was not implemented")

    @abstractmethod
    def get_artist(self, artist_id: str):
        raise NotImplementedError("Method get_artist was not implemented")
