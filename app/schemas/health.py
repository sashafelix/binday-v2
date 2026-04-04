'''Pydantic schemas for health endpoint and standard response envelope.'''

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel


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
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


def err(data: Any) -> ApiResponse:
    """Wrap error response data in the standard envelope."""
    return ApiResponse(
        success=False,
        data=data,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


class HealthResponse(BaseModel):
    """Schema for health check response payload."""

    app_version: str
    current_timestamp: str