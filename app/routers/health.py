from fastapi import APIRouter
from app.services.health_service import get_health
from app.schemas.health import HealthResponse
from app.main import ok

router = APIRouter(prefix="/api/v1", tags=["Health"])

@router.get("/health", response_model=HealthResponse, summary="Health check")
async def health_check() -> dict:
    """
    Health endpoint returning version and timestamp wrapped in the standard envelope.
    """
    health_data = await get_health()
    return ok(health_data).model_dump()