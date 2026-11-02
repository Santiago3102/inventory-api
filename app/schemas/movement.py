"""Pydantic schemas for stock movements."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MovementCreate(BaseModel):
    """Body of an entry or exit request."""

    model_config = ConfigDict(str_strip_whitespace=True)

    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    note: str | None = Field(default=None, max_length=255)


class MovementResponse(BaseModel):
    """A registered movement, as stored in the history."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    type: str
    quantity: int
    stock_before: int
    stock_after: int
    note: str | None
    created_at: datetime