#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
        creates an object from a JSON file
        
        Args:
            filename: file from which object is found
    """

    with open(filename, encoding='utf8') as f:
        return json.loads(f.open(filename))
