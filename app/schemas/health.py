'''Health endpoint response schema.'''

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Schema for health check response."""
    version: str = Field(..., description="Application version")
    timestamp: str = Field(..., description="Current UTC timestamp in ISO-8601 format")