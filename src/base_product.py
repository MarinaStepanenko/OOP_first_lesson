from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
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
