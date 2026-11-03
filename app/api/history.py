"""Movement history endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.movement import MovementResponse
from app.services import history_service

router = APIRouter(tags=["history"])


@router.get("/history/{product_id}", response_model=list[MovementResponse])
def get_history(product_id: int, db: Session = Depends(get_db)) -> list[MovementResponse]:
    """Lists the movements of a product, newest first."""
    movements = history_service.list_history(db, product_id)
    return [MovementResponse.model_validate(movement) for movement in movements]