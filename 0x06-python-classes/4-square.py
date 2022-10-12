#!/usr/bin/python3
"""Working with classes, python OOP"""


class Square():
    """Class that tries to model a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property for retrieving size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Instance method that computes area of a square
            Args:
                self
        """
        return (self.__size * self.__size)
