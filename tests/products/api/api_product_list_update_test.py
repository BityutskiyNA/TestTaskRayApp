import pytest


@pytest.mark.django_db
def test_product_view(client, product):
    data = {
        'name': 'test1',
        'article': 'a-1',
        'description': 'test',
        'product_type': 'foods',
    }
    response = client.patch(f'/api/{product.pk}/update/',
                            data,
                            content_type='application/json')
    expected_response = {
        'id': product.pk,
        'images': [],
        'name': 'test1',
        'article': 'a-1',
        'description': 'test',
        'product_type': 'foods',
        'price': 0,
        'quantity': 0
    }
    assert response.status_code == 200
    assert response.data == expected_response
