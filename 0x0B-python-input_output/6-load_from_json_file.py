#!/usr/bin/python3

"""Python file IO, loading from json file"""
import json


def load_from_json_file(filename):
    """Load from a json file"""
    with open(filename) as file_obj:
        contents = json.load(file_obj)
    return contents
