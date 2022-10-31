#!/usr/bin/python3

"""Python OOP, unit tests and file IO"""
import json


class Base:
    """Base class for all other classes"""

    __nb_of_objects = 0

    def __init__(self, id=None):
        if id == None:
           Base.__nb_of_objects += 1
           self.id = Base.__nb_of_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_of_objs):
        json_file ="{}.json".format(cls.__name__)
        obj_list = []

        if list_of_objs is None:
            pass
        else:
            for l in range(len(list_of_objs)):
                obj_list.append(list_of_objs[l].to_dictionary())

        obj_list_str = cls.to_json_string(obj_list)

        with open(json_file, 'w') as file_obj:
            file_obj.write(obj_list_str)
