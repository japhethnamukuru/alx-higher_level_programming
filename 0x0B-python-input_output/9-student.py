#!/usr/bin/python3

""""Python file IO, returning a class variables"""


class Student:
    """Student class that attempts to model a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrive instance dict"""

        return self.__dict__
