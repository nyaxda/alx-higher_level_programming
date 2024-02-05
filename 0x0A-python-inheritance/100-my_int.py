#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """A class that inherits from int."""

    def __eq__(self, value):
        """Override the equality operator."""
        return self.real != int(value)

    def __ne__(self, other):
        """Override the inequality operator."""
        return self.real == int(other)
