import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health
from app.core.config import Settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    settings = Settings()
    app = FastAPI(title="binday-v2", version=settings.app_version)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)

    return app


app = create_app()