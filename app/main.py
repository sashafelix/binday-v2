import logging
import uuid
from datetime import datetime, timezone
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health
from app.core.config import settings

logger = logging.getLogger("uvicorn.access")
logger.setLevel(logging.INFO)

app = FastAPI(title="binday-v2", version=settings.APP_VERSION)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    logger.info(
        {
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    )
    response = await call_next(request)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")