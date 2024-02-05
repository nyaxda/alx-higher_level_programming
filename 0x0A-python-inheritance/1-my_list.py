#!/usr/bin/python3
"""This module contains a class that inherits from list"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
