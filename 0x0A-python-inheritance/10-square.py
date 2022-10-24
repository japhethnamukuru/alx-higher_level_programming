#!/usr/bin/python3

"""Python OOP, subclassing a class through inheritance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rectangle inherits from BaseGeometry"""

    def __init__(self, size):
        """Initialize istance attributes"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Compute the area"""

        return (self.__size * self.__size)

    def __str__(self):
        """object representation"""

        return "[Rectangle] {}/{}".format(self.__size, self.__size)
