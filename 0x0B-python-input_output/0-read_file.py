#!/usr/bin/python3

"""Read a text file and display it to std out"""


def read_file(filename=""):
    """Read a file and print its contents"""
    with open(filename, 'r', encoding="utf-8") as file_obj:
        text = file_obj.read()
        print(text)
