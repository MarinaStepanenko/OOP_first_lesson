from src.category import Category


def test_category_init(category):
    assert category.description == "Современные телефоны"
    assert category.name == "Телефоны"
    assert len(category.products) == 1

    assert Category.category_count == 2
    assert Category.product_count == 8
