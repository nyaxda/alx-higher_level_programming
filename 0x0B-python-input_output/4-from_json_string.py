#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
        this function returns an object represented by a JSON string

        Args:
            obj: JSON string representation to be loaded
    """

    return json.loads(my_str)
