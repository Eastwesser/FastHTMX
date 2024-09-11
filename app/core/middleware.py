import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette_csrf import CSRFMiddleware

from app.core.config import settings

logger = logging.getLogger("middleware")


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        logger.info(f"Request URL: {request.url}")
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response


def setup_middleware(app):
    # Подключение CSRF Middleware
    app.add_middleware(
        CSRFMiddleware,
        secret=settings.CSRF_SECRET,  # Убедитесь, что это значение находится в конфигурации
    )

    # Подключение Log Middleware
    app.add_middleware(LogMiddleware)
