#!/usr/bin/python3
"""Module with method is the type of the class"""

def is_kind_of_class(obj, a_class):
    """ Method that returns True if the object is an instance of a class, or if the object is
    an instance of a class that inherited from"""

    return isinstance(obj, a_class)
