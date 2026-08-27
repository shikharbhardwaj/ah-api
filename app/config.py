from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    ah_base_url: str = "https://api.ah.nl"
    ah_user_agent: str = "Appie/9.27.0"
    # Comma-separated list of allowed CORS origins. Empty (default) disables
    # cross-origin browser access entirely — the app carries purchase history.
    cors_origins: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def cors_origin_list(self) -> list[str]:
        """Parse CORS_ORIGINS env var (comma-separated) into a list."""
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
