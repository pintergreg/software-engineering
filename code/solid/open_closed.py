# https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
import math


class Shape:
    pass


class AreaInterface:
    def area(shape: Shape) -> float:
        pass


class Square(Shape, AreaInterface):
    def __init__(self, width: float):
        self.width = width

    def area(self) -> float:
        return self.width**2


class Circle(Shape, AreaInterface):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(self.radius**2 * math.pi, 2)


class AreaCalculator:
    def sum(self, shapes: list[Shape]) -> float:
        result = 0
        for shape in shapes:
            result += shape.area()

        return result

    def sum_short(self, shapes: list[Shape]) -> float:
        return sum([i.area() for i in shapes])


if __name__ == "__main__":
    s = Square(2)
    print(s.area())
    c = Circle(2)
    print(c.area())

    ac = AreaCalculator()
    print(ac.sum2([s, c]))
