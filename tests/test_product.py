from src.product import Product


def test_product_init(first_product, second_product):
    assert first_product.name == "LG PC"
    assert first_product.description == "Это описание продукта"
    assert first_product.price == 156.78
    assert first_product.quantity == 2

    assert second_product.name == "Samsung Phone"
    assert second_product.quantity == 6
    assert second_product.price == 2990.99
    assert second_product.description == "Это второе описание"


def test_new_product():
    new_products = {
        "name": "Samsung 456",
        "description": "Описание",
        "price": 25600,
        "quantity": 1,
    }
    result = Product.new_product(new_products)
    assert result.price == 25600
    assert result.description == "Описание"
    assert result.name == "Samsung 456"
    assert result.quantity == 1


def test_new_product_existing():
    product_list = [Product("Samsung 456", "Описание", 25600, 1)]
    try_new = {
        "name": "Samsung 456",
        "description": "Описание",
        "price": 25600,
        "quantity": 1,
    }
    result = Product.new_product(try_new, product_list)
    assert result.quantity == 2

    product_list2 = [Product("Samsung 455", "Описание", 25600, 1)]
    try_new2 = {
        "name": "Samsung 455",
        "description": "Описание",
        "price": 30600,
        "quantity": 1,
    }
    result2 = Product.new_product(try_new2, product_list2)
    assert result2.price == 30600
    assert result2.quantity == 2


def test_price_getter():
    product1 = Product("iPhone", "Смартфон", 50000, 10)
    price_product = product1.price
    assert price_product == 50000


def test_price_setter_zero(capsys, monkeypatch):
    product1 = Product("iPhone", "Смартфон", 50000, 10)
    value = 0
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product1.price = value
    captured = capsys.readouterr()
    output = captured.out
    assert "Цена не должна быть нулевая или отрицательная" in output

    product2 = Product("iPhone10", "Смартфон", 50000, 10)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product2.price = 30000
    assert product2.price == 50000

    product3 = Product("iPhone11", "Смартфон", 50000, 10)
    product3.price = 60000
    assert product3.price == 60000
