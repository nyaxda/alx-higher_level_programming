#!/usr/bin/python3
import json
"""function that returns the JSON representation
of an object (string)"""


def to_json_string(my_obj):
    """
    returns JSON representation of an object
    
    Args:
        my_obj: object
    """

    return json.dumps(my_obj)
