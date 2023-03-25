#!/usr/bin/python3
"""Make a Rectangle Class of Basegeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """Initializes Square's side size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Square's description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
