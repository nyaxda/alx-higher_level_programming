#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Read
    Args:
        filename: name of file
    """

    with open(filename, encoding='utf') as f:
        read_data = f.read()
    print(read_data, end="")
