"""Stock movement endpoints (entries and exits)."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.movement import MovementCreate, MovementResponse
from app.services import movement_service

router = APIRouter(prefix="/movements", tags=["movements"])


@router.post("/entries", response_model=MovementResponse, status_code=status.HTTP_201_CREATED)
def create_entry(data: MovementCreate, db: Session = Depends(get_db)) -> MovementResponse:
    """Registers a stock entry (units received)."""
    movement = movement_service.register_entry(db, data)
    return MovementResponse.model_validate(movement)


@router.post("/exits", response_model=MovementResponse, status_code=status.HTTP_201_CREATED)
def create_exit(data: MovementCreate, db: Session = Depends(get_db)) -> MovementResponse:
    """Registers a stock exit (units sold or removed). Fails if stock is not enough."""
    movement = movement_service.register_exit(db, data)
    return MovementResponse.model_validate(movement)