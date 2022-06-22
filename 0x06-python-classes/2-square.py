#!/usr/bin/python3
""" This is the "Square" module. """


class Square:
    """ 
    Represents a square.
    Private instance attribute: size.
    Instatiation with optional size.
    """

    def __init__(self, size=0):
        """ Initialize data """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
