from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastHTMX!"}


def test_clicker_index():
    response = client.get("/api/v1/clicker/")
    assert response.status_code == 200
    assert "count" in response.text


def test_products_list():
    response = client.get("/api/v1/products/")
    assert response.status_code == 200
    assert "Product 1" in response.text
