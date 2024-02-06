#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
        this function writes an Object to a text file
        using a JSON representation

        Args:
            my_obj: JSON represented string
            filename: file to be written to
    """

    with open(filename, 'w', encoding='utf8') as f:
        return json.dumps(my_obj)
