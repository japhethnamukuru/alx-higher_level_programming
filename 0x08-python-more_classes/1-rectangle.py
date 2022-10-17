#!/usr/bin/python3

"""Python OOP, classes and objects"""


class Rectangle():
    """A class for creating rectangle instances"""

    def __init__(self, width=0, height=0):
        """Initilize width and height"""
        self.width = width
        self.height = height

        @property
        def width(self):
            """fetch width"""
            return self.__width

        @property
        def height(self):
            """height getter"""
            return self.__height
        
        @width.setter
        def width(self, value):
            """width setter"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @height.setter
        def height(self, value):
            """height setter"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
