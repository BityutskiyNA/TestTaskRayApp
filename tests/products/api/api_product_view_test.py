import pytest


@pytest.mark.django_db
def test_product_view(client, product):
    response = client.get(f"/api/view/{product.pk}/")
    expected_response = {
        "id": product.pk,
        "images": [],
        "created": response.data["created"],
        "updated_at": response.data["updated_at"],
        "name": "test",
        "article": "a-1",
        "description": "test",
        "product_type": "foods",
        "price": 0,
        "quantity": 0,
    }
    assert response.status_code == 200
    assert response.data == expected_response
