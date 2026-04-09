from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from app.models.collection_cache import CollectionCache
from app.schemas.collection_schema import CollectionMinimalResponse


def get_next_collection(db: Session, user_address: str) -> Optional[CollectionMinimalResponse]:
    """Return the next scheduled collection for the given user.

    The query selects the first collection whose ``scheduled_at`` is in the future,
    ordered by the earliest ``scheduled_at`` timestamp.
    If no collection is found, ``None`` is returned.
    """
    result = (
        db.query(CollectionCache)
        .filter(
            CollectionCache.user_address == user_address,
            CollectionCache.scheduled_at > datetime.utcnow(),
        )
        .order_by(CollectionCache.scheduled_at.asc())
        .first()
    )
    if result is None:
        return None
    return CollectionMinimalResponse(
        collection_id=result.collection_id,
        title=result.title,
        scheduled_at=result.scheduled_at,
    )