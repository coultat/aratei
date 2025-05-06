from typing import ClassVar, Self

from pydantic_settings import BaseSettings


class InternalCachedBaseSettings(BaseSettings):
    _cached_instance: ClassVar[Self | None] = None

    @classmethod
    def load(cls) -> Self:
        """Get settings from the usual places - env, secret files. Caches the result indefinitely."""
        if cls._cached_instance is None:
            cls._cached_instance = cls()
        return cls._cached_instance  # type: ignore[return-value]
