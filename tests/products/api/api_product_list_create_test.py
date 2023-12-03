import pytest


@pytest.mark.django_db
def test_product_create_view(client):
    data = {
        'name': 'test',
        'article': 'a-1',
        'description': 'test',
        'product_type': 'foods',
    }
    response = client.post('/api/create/',
                           data,
                           content_type='application/json')
    expected_response = {
        'id': 1,
        'images': [],
        'created': response.data['created'],
        'updated_at': response.data['updated_at'],
        'name': 'test',
        'article': 'a-1',
        'description': 'test',
        'product_type': 'foods',
        'price': 0,
        'quantity': 0
    }
    assert response.status_code == 201
    assert response.data == expected_response

@pytest.mark.django_db
def test_product_create_view_not_product_type(client):
        data = {
            'name': 'test',
            'article': 'a-1',
            'description': 'test',
        }
        response = client.post('/api/create/',
                               data,
                               content_type='application/json')

        assert response.status_code == 400
