#!/usr/bin/python3
"""File that defines a square by size"""


class Square:
    """Class that defines a square by size"""
    def __init__(self, size=0):
        """_summary_
        Args:
        size (_type_): _description_
        """
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
