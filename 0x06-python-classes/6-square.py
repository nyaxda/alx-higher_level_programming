#!/usr/bin/python3
"""File that defines a square by size"""


class Square:
    """Class that defines a square by size"""
    def __init__(self, size=0, position=(0, 0):
        """_summary_
        Args:
        size (_type_): _description_
        """
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

     def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range (self.__position[1]):
                print("")
            for j in range(self.__size):
                for e in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
                
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value
        if type(a) is not int or type(b) is not int or a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
