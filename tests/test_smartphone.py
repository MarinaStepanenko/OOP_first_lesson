import pytest


def test_smartphone_init(smartphone):
    assert smartphone.name == "New phone"
    assert smartphone.quantity == 5
    assert smartphone.description == "best phone for you"
    assert smartphone.price == 18000
    assert smartphone.color == "pink"
    assert smartphone.memory == 120
    assert smartphone.model == "S245"
    assert smartphone.efficiency == 55.5


def test_smartphone_add(smartphone, smartphone1):
    assert smartphone + smartphone1 == 91000


def test_smartphone_add_int(smartphone1):
    with pytest.raises(TypeError):
        smartphone1 + 1


def test_smartphone_add_wrong_class(category):
    with pytest.raises(TypeError):
        category.add_product("не продукт")
