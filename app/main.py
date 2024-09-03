from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.csrf import CSRFMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.FastHTMX,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Подключение статики и шаблонов
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Подключение маршрутов
app.include_router(api_router, prefix=settings.API_V1_STR)

# Подключение CSRF Middleware
app.add_middleware(CSRFMiddleware, secret=settings.CSRF_SECRET)


# Маршрут для главной страницы
@app.get("/")
async def root():
    return {"message": "Welcome to FastHTMX!"}
