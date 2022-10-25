#!/usr/bin/python3

"""Python file IO, saving to a file using json"""
import json


def save_to_json_file(my_obj, filename):
    """Write to a files using json"""
    with open(filename, 'w') as file_obj:
        json.dump(my_obj, file_obj)
