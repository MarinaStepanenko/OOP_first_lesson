from typing import Any


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if self.__price <= 0 or value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        if value < self.__price:
            answer = input(
                "Введите 'y' если подтверждаете новую цену, 'n' если хотите отменить"
            )
            if answer == "y":
                self.__price = value
        else:
            self.__price = value

    @classmethod
    def new_product(cls, parameters: dict, product_list: Any | None = None):
        if not product_list:
            product_list = []
        for existing_product in product_list:
            if existing_product.name == parameters["name"]:
                final_price = max(existing_product.price, parameters["price"])
                final_quantity = existing_product.quantity + parameters["quantity"]

                existing_product.price = final_price
                existing_product.quantity = final_quantity
                return existing_product

        return cls(
            parameters["name"],
            parameters["description"],
            parameters["price"],
            parameters["quantity"],
        )
