from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/examples", response_class=HTMLResponse)
async def examples(request: Request):
    return templates.TemplateResponse("examples/index.html", {"request": request})
