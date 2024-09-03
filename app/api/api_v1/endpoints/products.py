from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def products_list(request: Request):
    products = ["Product 1", "Product 2", "Product 3"]
    return templates.TemplateResponse(
        "products/list.html", {"request": request, "products": products}
    )
