#!/usr/bin/python3
"""module with method inherits_from"""


def inherits_from(obj, a_class):
    """Return True if an object is an instance of a class
    that inherited from"""
    return not type(obj) == a_class and isinstance(obj, a_class)
