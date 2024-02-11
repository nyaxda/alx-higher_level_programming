#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method."""
        self.__width = value
    
    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Height setter method"""
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the rectangle."""
        return self.__x
    
    @x.setter
    def x(self, value):
        """x setter method."""
        self.__x = value
    
    @property
    def y(self):
        """gets the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method."""
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiates a new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
