#!/usr/bin/python3

"""Python file IO, return a string representation from json"""
import json


def from_json_string(my_str):
    """Return a string representation of a json object"""
    return json.loads(my_str)
