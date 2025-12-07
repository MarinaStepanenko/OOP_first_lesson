import json
import os.path

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """
    Передаем путь до файла json, читаем его и возвращаем словарь.
    """
    fullpath = os.path.abspath(path)
    with open(fullpath, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: dict) -> list[Category]:
    """
    Передаем словарь и вытаскиваем данные по категориям и продуктам, превращая их в объекты.
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    product_data = read_json("../data/products.json")
    print(product_data)
    categories_created = create_objects_from_json(product_data)
    print(categories_created)
    print(categories_created[0].products)
