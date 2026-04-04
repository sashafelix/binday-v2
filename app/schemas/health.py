from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Any


class HealthResponse(BaseModel):
    """Schema representing health check response data."""
    version: str
    timestamp: str


class ApiResponse(BaseModel):
    """Standard API response envelope."""
    success: bool
    data: Any
    timestamp: str


def ok(data: Any) -> ApiResponse:
    """Wrap successful response data in the standard envelope."""
    return ApiResponse(
        success=True,
        data=data,
        timestamp=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    )


def err(data: Any) -> ApiResponse:
    """Wrap error response data in the standard envelope."""
    return ApiResponse(
        success=False,
        data=data,
        timestamp=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    )