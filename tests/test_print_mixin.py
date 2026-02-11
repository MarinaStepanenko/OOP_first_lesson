from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product(name="LG PC", description="Это описание продукта", price=156.78, quantity=2)
    message = capsys.readouterr()
    assert message.out.strip() == "Product, LG PC, Это описание продукта, 156.78, 2"

    Smartphone(
        name="New phone",
        description="best phone for you",
        price=18000,
        quantity=5,
        efficiency=55.5,
        model="S245",
        memory=120,
        color="pink",
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone, New phone, best phone for you, 18000, 5"

    LawnGrass(
        name="хорошая трава",
        description="трава не годится ни на что",
        price=150,
        quantity=2,
        country="USA",
        germination_period="2 дня",
        color="синий",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass, хорошая трава, трава не годится ни на что, 150, 2"
    )
