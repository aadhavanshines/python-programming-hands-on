import math
from dataclasses import dataclass


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_cost(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly_cost(self):
        return super().yearly_cost() + self.bonus


class Fraction:
    def __init__(self, top, bottom):
        if bottom == 0:
            raise ZeroDivisionError("bottom can't be zero")
        g = math.gcd(top, bottom)
        sign = -1 if bottom < 0 else 1
        self.top = sign * top // g
        self.bottom = sign * bottom // g

    def __add__(self, other):
        return Fraction(
            self.top * other.bottom + other.top * self.bottom,
            self.bottom * other.bottom,
        )

    def __eq__(self, other):
        return (self.top, self.bottom) == (other.top, other.bottom)

    def __str__(self):
        return f"{self.top}/{self.bottom}"


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    print(Manager("Ana", 5000, 8000).yearly_cost())
    print(Fraction(1, 2) + Fraction(1, 3), Fraction(2, 4) == Fraction(1, 2))
    print(Point(0, 0).distance_to(Point(3, 4)))
