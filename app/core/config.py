from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    JWT_SECRET_KEY: str
    DATABASE_URL: str
    APP_VERSION: str = "unknown"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()