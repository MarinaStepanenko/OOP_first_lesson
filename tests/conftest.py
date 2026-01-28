import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone():
    return Smartphone(
        name="New phone",
        description="best phone for you",
        price=18000,
        quantity=5,
        efficiency=55.5,
        model="S245",
        memory=120,
        color="pink",
    )


@pytest.fixture
def smartphone1():
    return Smartphone(
        name="Old phone",
        description="worst phone for you",
        price=1000,
        quantity=1,
        efficiency=15.5,
        model="V5",
        memory=32,
        color="yellow",
    )


@pytest.fixture
def grass():
    return LawnGrass(
        name="хорошая трава",
        description="трава не годится ни на что",
        price=150,
        quantity=2,
        country="USA",
        germination_period="2 дня",
        color="синий",
    )


@pytest.fixture
def grass1():
    return LawnGrass(
        name="плохая трава",
        description="трава ужас",
        price=15,
        quantity=1,
        country="Canada",
        germination_period="3 дня",
        color="голубой",
    )
