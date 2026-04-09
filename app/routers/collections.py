from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from typing import Any, Dict

from app.dependencies.auth import get_current_user
from app.services.collection_service import CollectionService
from app.schemas.collection_schema import CollectionMinimalResponse, ApiResponse

router = APIRouter(
    prefix="/api/v1/collections",
    tags=["collections"]
)

@router.get(
    "/next",
    response_model=ApiResponse[Dict[str, Any]],
    responses={
        200: {"description": "Success"},
        401: {"description": "Unauthorized"},
    },
)
async def get_next_collection(
    current_user: dict = Depends(get_current_user),
) -> ApiResponse[CollectionMinimalResponse]:
    """
    Returns the minimal collection payload for the authenticated user.
    If no upcoming collection exists, returns an empty data object.
    """
    service = CollectionService()
    collection = await service.get_next_collection(current_user["address"])
    if collection is None:
        data = {}
    else:
        data = collection
    return ApiResponse(success=True, data=data, timestamp=datetime.utcnow().isoformat())