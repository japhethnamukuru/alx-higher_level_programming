#!/usr/bin/python3

"""Python OOP, subclassing a class through inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize instance attributes"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Compute the area"""

        return (self.__width * self.__height)

    def __str__(self):
        """object representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
