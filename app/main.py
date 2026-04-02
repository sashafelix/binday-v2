import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health
from app.core.config import Settings, get_settings

def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    settings: Settings = get_settings()
    app = FastAPI(title="Health Service", version=settings.app_version)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers with the required prefix
    app.include_router(health.router, prefix="/api/v1")

    return app

app = create_app()