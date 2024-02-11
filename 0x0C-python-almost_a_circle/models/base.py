#!/usr/bin/python3
"""Defines a base class for all models in the project."""


class Base:
    """Represents the BaseModel class."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
