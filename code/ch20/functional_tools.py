from functools import partial, reduce

prices = [12.5, 8.0, 30.0, 4.25]

with_tax = list(map(lambda p: round(p * 1.2, 2), prices))
expensive = list(filter(lambda p: p > 10, prices))
print(with_tax)
print(expensive)

# The same with comprehensions, which most Python programmers prefer:
print([round(p * 1.2, 2) for p in prices])
print([p for p in prices if p > 10])

product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(product)


def power(base, exponent):
    return base**exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(square(9), cube(2))
