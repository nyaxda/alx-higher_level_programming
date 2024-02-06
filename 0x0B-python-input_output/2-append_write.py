#!/usr/bin/python3
"""appends a string at the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """
        this function appends a string at the end of the text file
        Args:
            filename: file to be appended to
            text: string to append
    """

    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
