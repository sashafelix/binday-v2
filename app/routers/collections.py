from __future__ import annotations

from datetime import datetime
from typing import Any

from fastapi import APIRouter, Depends, status

from app.dependencies.auth import AuthUser, get_current_user
from app.dependencies.database import get_db
from app.schemas.collection_schema import CollectionMinimalResponse
from app.schemas.common import ApiResponse
from app.services.collection_service import get_next_collection

router = APIRouter(
    prefix="/api/v1/collections",
    tags=["collections"],
)


@router.get(
    "/next",
    response_model=ApiResponse[CollectionMinimalResponse | dict],
    status_code=status.HTTP_200_OK,
    summary="Get next scheduled collection for the authenticated user",
)
async def next_collection(
    current_user: AuthUser = Depends(get_current_user),
    db: Any = Depends(get_db),
) -> ApiResponse[CollectionMinimalResponse | dict]:
    """Return the minimal collection payload for the authenticated user.

    If no upcoming collection exists, `data` is an empty object.
    """
    collection = await get_next_collection(current_user.address, db)
    payload: CollectionMinimalResponse | dict = collection.dict() if collection else {}
    return ApiResponse(success=True, data=payload, timestamp=datetime.utcnow())