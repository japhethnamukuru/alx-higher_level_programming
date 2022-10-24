#!/usr/bin/python3
"""Python OOP, a function that returns an objects namespace"""


def lookup(obj):
    """Return a list of an objects globals"""
    return list(dir(obj))
