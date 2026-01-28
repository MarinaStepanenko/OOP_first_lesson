import pytest


def test_lawngrass_init(grass):
    assert grass.color == "синий"
    assert grass.country == "USA"
    assert grass.germination_period == "2 дня"
    assert grass.quantity == 2
    assert grass.price == 150
    assert grass.name == "хорошая трава"
    assert grass.description == "трава не годится ни на что"


def test_lawngrass_add_success(grass, grass1):
    assert grass + grass1 == 315


def test_lawngrass_add_int(grass):
    with pytest.raises(TypeError):
        grass + 3


def test_lawngrass_add_wrong_category(grass1, smartphone1):
    with pytest.raises(TypeError):
        grass1 + smartphone1
