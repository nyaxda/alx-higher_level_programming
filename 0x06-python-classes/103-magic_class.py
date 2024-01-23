#!/usr/bin/python3
import math
"""import math"""

class _MagicClass:
    """Magic class"""
    def __init__(self, radius=0):
        """an init function"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area function"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circumference function"""
        return 2 * math.pi * self.__radius
    