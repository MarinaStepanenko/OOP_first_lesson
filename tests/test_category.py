from src.category import Category
from src.product import Product
from tests.conftest import second_product


def test_category_init():
    second_product = Product(
        name="Samsung Phone",
        description="Это второе описание",
        price=2990.99,
        quantity=6,
    )
    category = Category(
        name="Телефоны",
        description="Современные телефоны",
        products=[second_product],
    )
    assert category.description == "Современные телефоны"
    assert category.name == "Телефоны"
    assert len(category.products) == 42

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_products():
    Category.product_count = 0
    second_product = Product(
        name="Samsung Phone",
        description="Это второе описание",
        price=2990.99,
        quantity=6,
    )
    category = Category(
        name="Телефоны",
        description="Современные телефоны",
        products=[],
    )
    category.add_product(second_product)

    assert Category.product_count == 1


def test_add_products_empty():
    Category.product_count = 0
    first_product = Product(
        name="LG PC", description="Это описание продукта", price=156.78, quantity=2
    )
    category = Category(
        name="Телефоны",
        description="Современные телефоны",
        products=[second_product],
    )
    category.add_product(first_product)

    assert Category.product_count == 2


def test_getter_many_products():
    products = [
        Product("iPhone", "Смартфон", 50000, 10),
        Product("Samsung", "Смартфон", 40000, 5),
        Product("Xiaomi", "Смартфон", 30000, 8),
    ]
    category = Category("Телефоны", "Современные технологии", products)
    result = category.products
    assert (
        category.products == "iPhone, 50000 руб. Остаток: 10 шт.\n"
        "Samsung, 40000 руб. Остаток: 5 шт.\n"
        "Xiaomi, 30000 руб. Остаток: 8 шт."
    )
    assert isinstance(result, str)
    lines = result.split("\n")
    assert len(lines) == 3
