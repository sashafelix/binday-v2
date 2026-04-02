from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Schema for health check response data."""
    version: str
    timestamp: str