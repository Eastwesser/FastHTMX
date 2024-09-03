from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def clicker_index(request: Request):
    count = 0  # Логика для работы с количеством кликов
    return templates.TemplateResponse(
        "clicker/index.html", {"request": request, "count": count}
    )


@router.post("/inc-click", response_class=HTMLResponse)
async def inc_click(request: Request):
    count = 1  # Логика для инкрементации счётчика
    return templates.TemplateResponse(
        "clicker/clicker-components/click-count.html", {"request": request, "count": count}
    )
