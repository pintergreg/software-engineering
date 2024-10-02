class Rectangle:

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def setWidth(self, width: int):
        self.__width = width

    def setHeight(self, height: int):
        self.__height = height

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getArea(self):
        return self.__width * self.__height


class Square(Rectangle):

    def __init__(self, width: int):
        super().setWidth(width)
        super().setHeight(width)

    def setWidth(self, width: int):
        super().setWidth(width)
        super().setHeight(width)

    def setHeight(self, height: int):
        super().setWidth(height)
        super().setHeight(height)


def getAreaTest(r: Rectangle):
    width = r.getWidth()
    r.setHeight(10)
    return f"Expected area of {width * 10}, got {r.getArea()}"


if __name__ == "__main__":
    r = Rectangle(2, 3)
    print(r.getArea())

    s = Square(2)
    print(s.getArea())

    print(getAreaTest(r))
    print(getAreaTest(s))
