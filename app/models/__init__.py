"""Import every model here so Alembic can discover them."""

from app.models.movement import Movement
from app.models.product import Product

__all__ = ["Movement", "Product"]