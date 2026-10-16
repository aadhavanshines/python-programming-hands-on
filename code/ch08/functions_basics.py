def greet(name):
    """Print a friendly greeting."""
    print(f"Hello, {name}!")


def area(width, height):
    """Return the area of a rectangle."""
    return width * height


def price_with_tax(price, rate=0.18):
    """Return the price including tax: 18% unless you say otherwise."""
    return round(price * (1 + rate), 2)


greet("Lena")
greet("Tom")
print("Area:", area(3, 4.5))
print("With tax:", price_with_tax(100))
print("With 5% tax:", price_with_tax(100, 0.05))
print("Keyword arguments:", price_with_tax(rate=0.12, price=250))
