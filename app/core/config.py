import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    database_url: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
    app_version: str = os.getenv("APP_VERSION", "unknown")
    secret_key: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()