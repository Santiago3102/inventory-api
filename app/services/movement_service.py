"""Business rules for stock movements. Owns the transaction (commit / rollback)."""

from sqlalchemy.orm import Session

from app.core.errors import BusinessRuleError, NotFoundError
from app.models.movement import Movement
from app.repositories import movement_repository, product_repository
from app.schemas.movement import MovementCreate
from app.services.product_service import PRODUCT_NOT_FOUND

ENTRY = "ENTRY"
EXIT = "EXIT"

INSUFFICIENT_STOCK = "Stock insuficiente. Stock disponible: {available}"


def register_entry(db: Session, data: MovementCreate) -> Movement:
    """Adds units to the stock of a product."""
    return _register(db, data, ENTRY)


def register_exit(db: Session, data: MovementCreate) -> Movement:
    """Removes units from the stock of a product. Stock can never go negative."""
    return _register(db, data, EXIT)


def _register(db: Session, data: MovementCreate, movement_type: str) -> Movement:
    """Updates the stock and stores the movement in ONE transaction.

    The product row is locked (SELECT ... FOR UPDATE) so two simultaneous
    requests on the same product are processed one after the other.
    """
    try:
        product = product_repository.get_for_update(db, data.product_id)
        if product is None:
            raise NotFoundError(PRODUCT_NOT_FOUND)

        stock_before = product.current_stock
        if movement_type == ENTRY:
            stock_after = stock_before + data.quantity
        else:
            if data.quantity > stock_before:
                raise BusinessRuleError(INSUFFICIENT_STOCK.format(available=stock_before))
            stock_after = stock_before - data.quantity

        product_repository.update_stock(db, product, stock_after)
        movement = movement_repository.create(
            db,
            Movement(
                product_id=product.id,
                type=movement_type,
                quantity=data.quantity,
                stock_before=stock_before,
                stock_after=stock_after,
                note=data.note,
            ),
        )
        db.commit()
    except Exception:
        db.rollback()
        raise
    return movement