#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)
