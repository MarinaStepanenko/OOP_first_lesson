from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1

    @property
    def products(self):
        products_list = []
        for product in self.__products:
            products_list.append(str(product))
        return "\n".join(products_list)
