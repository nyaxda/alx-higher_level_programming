#!/usr/bin/python3
"""
This module contains a class that inherits from list
"""


class MyList(list):
    """
    inherits from list and has a method that prints the list,
     but sorted
    """
    
    def print_sorted(self):
        """
            prints the list, but sorted

            Args:
                self (list): list to sort and print

            Returns:
                None
        """
        print(sorted(self))
