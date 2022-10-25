#!/usr/bin/python3

"""Python file IO, saving arguments to a python file"""
import sys

if __name__ == '__main__':
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file


    try:
       items = load_from_json("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json(items, 'add_item.json')
