from datetime import datetime, timezone
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Schema representing the health status payload."""
    database: str = Field(..., description="Database connectivity status")
    next_scheduled_refresh: str = Field(
        ..., description="ISO‑8601 UTC timestamp of the next scheduled health refresh"
    )
    last_refresh: str = Field(
        ..., description="ISO‑8601 UTC timestamp of the last health refresh"
    )
    total_users: int = Field(..., description="Total number of registered users")
    version: str = Field(..., description="Application version")
    status: str = Field(..., description="Overall health status")
    timestamp: str = Field(..., description="Current ISO‑8601 UTC timestamp at request time")