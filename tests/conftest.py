from pytest_factoryboy import register

from tests.factores import ProductFactory

pytest_plugins = "tests.fixtures"

register(ProductFactory)
