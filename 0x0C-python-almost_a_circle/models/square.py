#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square.
        Private instance attributes:
            size: The size of the square.
            x: The x coordinate of the square.
            y: The y coordinate of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square.
        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int, optional): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
    