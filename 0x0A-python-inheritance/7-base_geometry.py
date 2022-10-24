#!/usr/bin/python3

"""Python OOP, empty class that attempts to model a geometry"""


class BaseGeometry:
    """Empty class for modelling geometry"""

    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
