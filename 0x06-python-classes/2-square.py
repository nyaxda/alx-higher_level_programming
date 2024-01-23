#!/usr/bin/python3
"""File that defines a square by size"""


class Square:
    """Class that defines a square by size"""
    def __init__(self, size=0):
        """_summary_
        Args:
        size (_type_): _description_
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
