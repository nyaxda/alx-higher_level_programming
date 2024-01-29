#!/usr/bin/python3
"""
    Rectangle Class
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

    # getting width value
    @property
    def width(self):
        """ width retriever """
        return self.__width

    # setting width value
    @width.setter
    def width(self, value):
        """ width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # getting height value
    @property
    def height(self):
        """ height retriever """
        return self.__height

    # setting width value
    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
