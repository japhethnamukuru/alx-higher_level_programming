#!/usr/bin/python3

"""Python3 file IO, returning  a json representation of a file"""
import json


def to_json_string(my_obj):
    """Return a json representation of a file object"""
    return json.dumps(my_obj)
