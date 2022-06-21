#!/usr/bin/python3
"""
This is the "Square"  module.
Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """ Defines a Square by size """
    def __init__(self, size):
        self.__size = size
