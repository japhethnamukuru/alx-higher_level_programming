#!/usr/python3
"""Python OOP, check if an object is kind of"""


def is_kind_of_class(obj, a_class):
    """Check of obj is an instance of, or if obj is an instance of class"""

    return True if isinstance(obj, a_class) else False
