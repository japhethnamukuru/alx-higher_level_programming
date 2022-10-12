#!/usr/bin/python3
"""Working with classes, python OOP"""


class Square():
    """Class that tries to model a square"""
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] is not int) or (value[1] is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            

    def area(self):
        """Instance method that computes area of a square
            Args:
                self
        """
        return (self.__size * self.__size)

    def my_print(self):
        my_value = self.__size
        if my_value == 0:
            print()
        else:
            for i in range(my_value):
                for j in range(my_value):
                    print("#", end='')
                print()
