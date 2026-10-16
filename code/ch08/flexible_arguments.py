def total(*numbers):
    """Add any number of numbers."""
    result = 0
    for n in numbers:
        result += n
    return result


def describe(name, **details):
    """Print a name followed by any details given as keyword arguments."""
    print(name)
    for key, value in details.items():
        print(f"  {key}: {value}")


print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))
describe("Pocket Library", version=3, books=4, language="Python")
