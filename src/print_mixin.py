class PrintMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}, {self.description}, {self.price}, {self.quantity}"


def check_mro():
    from src.product import Product  # Локальный импорт внутри функции

    print(Product.__mro__)


if __name__ == "__main__":
    check_mro()
