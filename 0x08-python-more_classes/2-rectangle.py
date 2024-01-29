#!/usr/bin/python3
"""
    Rectangle
"""


class Rectangle:
    """ Defines the width and height of a rectangle

    Args:
        width: breath of a rectangle
        height: length of a rectangle
    """
    def __init__(self, width=0, height=0):
        """ instantiation of width and height """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    @property
    def width(self):
        """ width retriever """
        return self.__width

    @width.setter
    def width(self, value):
        """ with setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height retriever """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ return the perimeter of the rectangle """
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)
