#!/usr/bin/python3
"""Make BaseGeometry class"""


class BaseGeometry():
    """Class BaseGeometry"""
    def area(self):
        """Function until now print the exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
