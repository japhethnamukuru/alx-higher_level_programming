#!/usr/bin/python3
"""Python OOP, check whethe a given object is a subclass of the given class"""


def inherits_from(obj, a_class):
    """Check of obj subclasses a_class"""

    return True if issubclass(type(obj), a_class) and type(obj) != a_class else False
