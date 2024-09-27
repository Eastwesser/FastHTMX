# Here we handle all routers
from fastapi import APIRouter

from ...core.config import settings
# from .endpoints import router as router_api_v1
from .api import api_router as router_api_v1

# Main API Router:
router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(
    router_api_v1,
)
