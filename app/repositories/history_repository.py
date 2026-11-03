"""Database access for the movement history."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.movement import Movement


def list_by_product(db: Session, product_id: int) -> list[Movement]:
    """Returns the movements of a product, newest first."""
    statement = (
        select(Movement)
        .where(Movement.product_id == product_id)
        .order_by(Movement.created_at.desc(), Movement.id.desc())
    )
    return list(db.scalars(statement).all())