# https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
import math


class Shape:
    pass


class Square(Shape):
    def __init__(self, width: float):
        self.width = width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius


class AreaCalculator:

    def sum(self, shapes: list[Shape]) -> float:
        result = 0
        for shape in shapes:
            if isinstance(shape, Square):
                result += shape.width**2
            elif isinstance(shape, Circle):
                result += shape.radius**2 * math.pi

        return round(result, 2)


if __name__ == "__main__":
    s = Square(2)
    c = Circle(2)

    ac = AreaCalculator()
    print(ac.sum([s, c]))
