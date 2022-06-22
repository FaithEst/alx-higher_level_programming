#!/usr/bin/python3
class Square:
    """
    Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """
    def __init__(self, size=0):
        """ Initialize size attribute. """
        self.__size = size

    @property
    def size(self):
        """ Get size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set size to equal value. """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square. """
        return self.__size ** 2

    def my_print(self):
        " Print the square with the character #. "
        if self.__size == 0:
            print()
        [print("#" * self.__size) for i in range(self.__size)]
