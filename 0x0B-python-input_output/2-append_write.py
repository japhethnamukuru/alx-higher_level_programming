#!/usr/bin/python3

"""Python file IO, appending to a file"""


def append_write(filename="", text=""):
    """Appending to a given file"""
    with open(filename, 'a', encoding="utf-8") as file_obj:
        append_characters = file_obj.write(text)
        return append_characters
