#!/usr/bin/python3
"""Python OOP, empty class that attempts to model a geometry"""


class BaseGeometry:
    """Empty class for modelling geometry"""

    def area(self):
        """Raise Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
