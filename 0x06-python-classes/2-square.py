#!/usr/bin/python3
"""Working with classes, python oop"""


class Square():
    """Square class that tries to model square"""
    def __init__(self, size=0):
        """The attribute size must be of type int
            Args:
                size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
