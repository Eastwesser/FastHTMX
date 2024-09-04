import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.csrf import CSRFMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse

from app.api.api_v1.api import api_router
from app.core.config import settings
from .api.api_v1 import router as api_router
from core.config import settings
from app.api.api_v1.endpoints.clicker import router as clicker_router
from app.api.api_v1.endpoints.products import router as products_router


app = FastAPI(
    title=settings.FastHTMX,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(api_router, prefix=settings.api.perfix)

# Подключение статики и шаблонов
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Подключение маршрутов
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(clicker_router, prefix="/clicker")
app.include_router(products_router, prefix="/products")

# Подключение CSRF Middleware
app.add_middleware(CSRFMiddleware, secret=settings.CSRF_SECRET)


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
