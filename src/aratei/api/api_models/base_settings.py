from typing import ClassVar, Self

from pydantic_settings import BaseSettings


class InternalCachedBaseSettings(BaseSettings):
    """Base class for settings with caching without vault access. Exists to prevent circular imports."""

    _cached_instance: ClassVar[Self | None] = None

    @classmethod
    def load(cls) -> Self:
        """Get settings from the usual places - env, secret files. Caches the result indefinitely."""
        # can't use cache decorator because of typing issues so we create our own cache
        if cls._cached_instance is None:
            cls._cached_instance = cls()
        return cls._cached_instance  # type: ignore[return-value]
