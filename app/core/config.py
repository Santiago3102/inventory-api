"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed configuration. Secrets live in environment variables, never in code."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    allowed_origins: str = "http://localhost:3000"

    @property
    def allowed_origins_list(self) -> list[str]:
        """Comma-separated ALLOWED_ORIGINS as a list."""
        return [o.strip() for o in self.allowed_origins.split(",") if o.strip()]


settings = Settings()