import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx_init
from starlette.requests import Request
from starlette_csrf import CSRFMiddleware

from app.api.api_v1 import router as api_router
# Импорт маршрутов
from app.api.api_v1.endpoints.clicker import router as clicker_router
from app.api.api_v1.endpoints.products import router as products_router
from app.core.config import settings
from app.create_fastapi_app import create_app

# Инициализация FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Подключение CSRF Middleware
app.add_middleware(
    CSRFMiddleware,
    secret="8148b7148634eeb37192a3d9ebcac7f877a8db21763f667ddaae3d065ba41ce0",
)

# Подключение маршрутов API
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(clicker_router, prefix="/clicker")
app.include_router(products_router, prefix="/products")

# Подключение статики и шаблонов
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Инициализация HTMX
htmx_init(templates=templates)


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Пример маршрута
@app.get("/examples")
async def examples():
    return {"message": "Examples page"}


# Пример маршрута для клика
@app.get("/clicker")
async def clicker():
    return {"message": "Clicker page"}


# Пример маршрута для получения данных
@app.get("/fetch-data", response_class=HTMLResponse)
async def fetch_data(request: Request):
    return {"message": "Data fetched successfully"}


# Обработка формы
@app.post("/submit", response_class=HTMLResponse)
async def submit_form(request: Request, name: str = Form(...)):
    return f"<p>Hello, {name}!</p>"


main_app = create_app(
    create_custom_static_urls=True,
)

main_app.include_router(
    api_router,
)

# Запуск приложения
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
