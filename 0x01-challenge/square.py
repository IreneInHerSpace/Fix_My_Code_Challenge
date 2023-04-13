#!/usr/bin/python3

class Square():

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        """ Area of the square """
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        return "Square with width {} and height {}"\
                .format(self.__width, self.__height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
