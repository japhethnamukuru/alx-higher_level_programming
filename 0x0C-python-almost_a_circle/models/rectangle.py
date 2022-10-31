#!/usr/bin/python3

"""Python OOP, creating classes and objects, writting tests"""
from .base import Base


class Rectangle(Base):
    """Rectangle class that models a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height setter"""

        return self.__height

    @height.setter
    def height(self, value):
        """hieight setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter x"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """get area of instance"""

        return (self.width * self.height)

    def display(self):
        """display rectangle using '#' """

        rectangle = self.y * '\n'
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + '\n'
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Assign args to each attribute"""

        if args is not None and len(args) != 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key,value)

    def to_dictionary(self):
        args_list = ['id', 'width', 'height', 'x', 'y']
        self_dict = {}

        for key in args_list:
            self_dict[key] = getattr(self, key)

        return self_dict

           
    def __str__(self):
        return "[Retangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)
