#!/usr/bin/python3

"""Python file permissions, writting to files"""


def write_file(filename="", text=""):
    """Writing to files"""
    with open(filename, 'w', encoding="utf-8") as file_obj:
        number_of_characters = file_obj.write(text)
    return number_of_characters
