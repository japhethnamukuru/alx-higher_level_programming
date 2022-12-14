#!/usr/bin/python3

"""class thet represents a rectangle"""


class Rectangle:
    """Rectangle class """

    def __init__(self, width=0, height=0):
        """the ractangle constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get area"""
        return self.width * self.height

    def perimeter(self):
        """get perimeter"""
        if (self.width == 0) or (self.height == 0):
            return 0
        return 2 * (self.width + self.height)
