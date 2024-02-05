#!/usr/bin/python3
"""This module contains a class that inherits from list"""


class MyList(list):
    """inherits from list"""
    def __init__(self):
        """initializes the object"""
        super().__init__(self)

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
