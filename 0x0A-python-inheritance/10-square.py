#!/usr/bin/python3
""" This module contains a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    it inherits from BaseGeometry

    Attributes:
    size (int): the size of the square

    Methods:
    __init__(self, size): instantiation with width and height
    area(self): returns the area of the rectangle
    __str__(self): returns a string representation of the rectangle
    """

    def __init__(self, size):
        """
        instantiation with width and height
        """
        super().integer_validator("width", size)
        self.__size = size

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns a string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
