import pytest

from products.models import Product


@pytest.mark.django_db
def test_product_delete(client):
    product = Product.objects.create(
        name='test',
        article='a-1',
        description='test'
    )
    response = client.delete(f'/api/{product.pk}/delete/')

    assert response.status_code == 204

