import factory.django

from products.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test"
    article = "a-1"
    description = "test"
    product_type = "foods"
