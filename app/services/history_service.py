"""Business rules for the movement history."""

from sqlalchemy.orm import Session

from app.core.errors import NotFoundError
from app.models.movement import Movement
from app.repositories import history_repository, product_repository
from app.services.product_service import PRODUCT_NOT_FOUND


def list_history(db: Session, product_id: int) -> list[Movement]:
    """Returns the movements of a product, newest first.

    Raises NotFoundError if the product does not exist. An empty list is a valid result.
    """
    if product_repository.get_by_id(db, product_id) is None:
        raise NotFoundError(PRODUCT_NOT_FOUND)
    return history_repository.list_by_product(db, product_id)