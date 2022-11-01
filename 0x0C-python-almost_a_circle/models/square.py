#!/usr/bin/python3

"""Python OOP"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        args_list = ['id', 'size', 'x', 'y']

        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if args_list[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, args_list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        args_list = ['id', 'size', 'x', 'y']
        sq_dict = {}

        for key in args_list:
            sq_dict[key] = getattr(self, key)

        return sq_dict


    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
