#!/usr/bin/python3
"""
Module for class that prevents dynamic instance creation

"""


class LockedClass:
    """ Prevent dynamic attribute creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """ The init method """
        pass

