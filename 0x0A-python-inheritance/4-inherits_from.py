#!/usr/bin/python3
"""This module contains a function that returns True if the object is an
instance of a class that inherited (directly or indirectly) from the
specified class, otherwise False"""


def inherits_from(obj, a_class):
    """
        Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class, otherwise False

        Args:
            obj (any): object to check
            a_class (class): class to check against

        Returns:
            bool: True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class, otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
