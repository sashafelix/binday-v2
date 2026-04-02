from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/dbname"
    APP_VERSION: str = "unknown"
    JWT_SECRET_KEY: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Export a singleton for easy import throughout the project
settings = Settings()