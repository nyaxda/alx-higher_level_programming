#!/usr/bin/python3
"""
This module contains an empty class BaseGeometry
"""


class BaseGeometry:
    """
    This class is the base class for geometry objects
    """

    def area(self):
        """
        This method raises an exception
        """

        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        This method validates the value passed to it

        Arguments:
        name (str): the name of the value
        value (int): the value to validate

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
