#!/usr/bin/python3
""" This module contains a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
