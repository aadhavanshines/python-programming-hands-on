from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1


def order_total(items: list[Item], discount: float = 0.0) -> float:
    """Total price of the items, minus a discount between 0 and 1."""
    total = sum(item.price * item.quantity for item in items)
    return round(total * (1 - discount), 2)


def cheapest(items: list[Item]) -> Item | None:
    return min(items, key=attrgetter("price"), default=None)


def parse_quantities(text: str) -> dict[str, int]:
    """'tea=2, milk=1' -> {'tea': 2, 'milk': 1}"""
    result: dict[str, int] = {}
    for part in text.split(","):
        name, _, number = part.partition("=")
        result[name.strip()] = int(number)
    return result


if __name__ == "__main__":
    basket = [Item("tea", 3.5, 2), Item("milk", 1.2)]
    print(order_total(basket, 0.1))
    found = cheapest(basket)
    print(found.name if found else "empty basket")
    print(parse_quantities("tea=2, milk=1"))
