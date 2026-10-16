class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


class Tally:
    """Count clicks, like a hand-held tally counter."""

    def __init__(self):
        self.count = 0

    def click(self, times=1):
        self.count += times
        return self.count

    def reset(self):
        self.count = 0


class Thermostat:
    def __init__(self, target=20.0, low=5.0, high=30.0):
        self.low = low
        self.high = high
        self.target = target

    def set_target(self, value):
        """Set the target within the allowed range; return it."""
        self.target = min(max(value, self.low), self.high)
        return self.target


if __name__ == "__main__":
    r = Rectangle(4, 4)
    print(r.area(), r.perimeter(), r.is_square())
    t = Tally()
    t.click()
    print(t.click(3))
    print(Thermostat().set_target(42))
