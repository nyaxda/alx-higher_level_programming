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
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        """size getter method."""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.id = kwargs['size']
            if 'x' in kwargs:
                self.id = kwargs['x']
            if 'y' in kwargs:
                self.id = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary represenetation of a Square"""
        return{"id": self.id, "size": self.size, "x": self.x, "y": self.y}
