"""Aggregates every router. Each component adds one line here."""

from fastapi import APIRouter

from app.api import health

api_router = APIRouter()
api_router.include_router(health.router)