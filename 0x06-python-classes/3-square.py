#!/usr/bin/python3
"""Working with classes, python OOP"""


class Square():
    """Class that tries to model a square"""
    def __init__(self, size=0):
        """Constructor methode for modelling square instances
            Args:
                size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Instance method that computes area of a square
            Args:
                self
        """
        return (self.__size * self.__size)
