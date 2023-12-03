import pytest


@pytest.mark.django_db
def test_product_list_view(client, product):
    expected_response = [{
        'id': product.pk,
        'name': product.name,
        'article': product.article,
        'description': product.description,
        'product_type': product.product_type,
        'price': product.price
    }]

    response = client.get('/api/')

    assert response.status_code == 200
    assert response.data == expected_response
