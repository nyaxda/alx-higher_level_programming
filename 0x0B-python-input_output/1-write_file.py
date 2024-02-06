#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename: file where it reads from
        text: string to be written to the file
    """

    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
