#!/usr/bin/python3
"""function that adds two integers"""
def add_integer(a, b=98):
    """add two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return (a + b)
