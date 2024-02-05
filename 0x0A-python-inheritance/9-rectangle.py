#!/usr/bin/python3
""" This module contains a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    it inherits from BaseGeometry

    Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle

    Methods:
    __init__(self, width, height): instantiation with width and height
    area(self): returns the area of the rectangle
    __str__(self): returns a string representation of the rectangle
    """

    def __init__(self, width, height):
        """
        instantiation with width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns a string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
