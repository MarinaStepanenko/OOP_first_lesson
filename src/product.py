from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        return total_price

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
