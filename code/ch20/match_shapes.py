from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Circle:
    center: Point
    radius: float


def describe(shape):
    match shape:
        case Point(x=0, y=0):
            return "the origin"
        case Point(x=0, y=y):
            return f"a point on the y-axis at {y}"
        case Point(x=x, y=y):
            return f"a point at ({x}, {y})"
        case Circle(center=Point(x=0, y=0), radius=r):
            return f"a circle of radius {r} around the origin"
        case Circle(radius=r) if r <= 0:
            return "an impossible circle"
        case Circle():
            return "a circle somewhere else"
        case {"type": "point", "x": x, "y": y}:
            return f"a point from JSON at ({x}, {y})"
        case _:
            return "something unknown"


for shape in [
    Point(0, 0),
    Point(0, 5),
    Point(2, 3),
    Circle(Point(0, 0), 4),
    Circle(Point(1, 1), -1),
    Circle(Point(1, 1), 2),
    {"type": "point", "x": 7, "y": 8},
    42,
]:
    print(describe(shape))
