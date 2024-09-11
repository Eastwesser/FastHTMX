import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_htmx import htmx_init
from starlette.requests import Request

from app.api.api_v1 import router as api_router
from app.api.api_v1.endpoints.clicker import router as clicker_router
from app.api.api_v1.endpoints.products import router as products_router
from app.api.api_v1.endpoints.examples import router as examples_router
from app.core.config import settings
from app.core.redis import init_redis, close_redis
from app.create_fastapi_app import create_app
from app.celery.celery_app import example_task
from .core.middleware import setup_middleware

# Инициализация FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Настройка middleware
setup_middleware(app)

# Подключение маршрутов API
app.include_router(api_router, prefix=settings.API_V1_STR)

# Подключение статики и шаблонов
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Инициализация HTMX
htmx_init(templates=templates)


# Маршрут для главной страницы
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/run-task")
async def run_task():
    result = example_task.delay()
    return {"task_id": result.id}


@app.on_event("startup")
async def startup():
    await init_redis()


@app.on_event("shutdown")
async def shutdown():
    await close_redis()


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
