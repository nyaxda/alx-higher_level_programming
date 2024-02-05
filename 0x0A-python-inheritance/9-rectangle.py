#!/usr/bin/python3
""" This module contains a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """it inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        instantiation with width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(width, height)
        """
        returns the area of the rectangle
        """
        return width * height
    
    def __str__(self):
        """
        returns a string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)\
