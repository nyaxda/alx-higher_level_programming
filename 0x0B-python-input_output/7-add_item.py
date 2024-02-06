#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""
import sys

if __name__ == '__main__':
    savejsonfile = __import__('5-save_to_json_file').save_to_json_file
    loadjsonfile = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        items = loadjsonfile(filename)
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    savejsonfile(items, filename)
