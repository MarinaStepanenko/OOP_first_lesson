def test_product_init(first_product, second_product):
    assert first_product.name == "LG PC"
    assert first_product.description == "Это описание продукта"
    assert first_product.price == 156.78
    assert first_product.quantity == 2

    assert second_product.name == "Samsung Phone"
    assert second_product.quantity == 6
    assert second_product.price == 2990.99
    assert second_product.description == "Это второе описание"
