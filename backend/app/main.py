import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import health
from .database import engine, Base

def create_app() -> FastAPI:
    """Create FastAPI application with CORS and router registration."""
    app = FastAPI(
        title="binday-v2 API",
        version=os.getenv("APP_VERSION", "unknown"),
    )

    # CORS (allow all for simplicity; adjust in production)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    app.include_router(health.router, prefix="/api/v1")

    @app.on_event("startup")
    async def on_startup() -> None:
        """Create database tables on startup if they do not exist."""
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    return app

app = create_app()