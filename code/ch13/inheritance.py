import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("each shape must define area()")

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "square"


shapes = [Circle(1), Rectangle(2, 3.5), Square(4)]
for shape in shapes:
    print(shape.describe())

print(isinstance(Square(1), Rectangle), issubclass(Circle, Shape))
