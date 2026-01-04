import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


@pytest.fixture
def first_product():
    return Product(
        name="LG PC", description="Это описание продукта", price=156.78, quantity=2
    )


@pytest.fixture
def second_product():
    return Product(
        name="Samsung Phone",
        description="Это второе описание",
        price=2990.99,
        quantity=6,
    )


@pytest.fixture
def category(second_product, first_product):
    a = Category(
        name="Планшеты",
        description="Современные планшеты",
        products=[first_product],
    )
    return Category(
        name="Телефоны",
        description="Современные телефоны",
        products=[second_product],
    )


@pytest.fixture
def product_iterator(category):
    return ProductIterator(category)
