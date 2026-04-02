'''FastAPI application factory with CORS and router registration.'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health

def get_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="binday-v2")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router, prefix="/api/v1")
    return app

app: FastAPI = get_app()