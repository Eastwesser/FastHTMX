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


@router.post("/products/add", response_class=HTMLResponse)
async def add_product(request: Request, name: str, price: float):
    # Логика для добавления нового продукта
    product_list = []
    new_product = {"name": name, "price": price}
    product_list.append(new_product)  # Добавляем продукт в список
    return templates.TemplateResponse(
        "products/components/item.html", {"request": request, "product": new_product}
    )
