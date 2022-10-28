#!/usr/bin/python3

"""Python OOP, unit tests and file IO"""


class Base:
    """Base class for all other classes"""

    __nb_of_objects = 0

    def __init__(self, id=None):
        if id == None:
           Base.__nb_of_objects += 1
           self.id = Base.__nb_of_objects
        else:
            self.id = id
