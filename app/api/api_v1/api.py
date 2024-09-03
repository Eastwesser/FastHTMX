# api.py — основной файл для маршрутизации API. Здесь объединяются все endpoints.
# app/api/api_v1/api.py

from fastapi import APIRouter

from app.api.api_v1.endpoints import clicker, products

api_router = APIRouter()

api_router.include_router(clicker.router, prefix="/clicker", tags=["clicker"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
