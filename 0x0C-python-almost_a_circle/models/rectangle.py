#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base
import json


class Rectangle(Base):
    """Represents a rectangle.
        Private instance attributes:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x coordinate of the rectangle.
            y: The y coordinate of the rectangle.
    """
    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """gets the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiates a new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """prints in the stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for k, v in kwargs.items():
                if k in attributes:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x, 'y': self.y
            }
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
