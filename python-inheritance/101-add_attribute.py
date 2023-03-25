#!/usr/bin/python3
"""Adds atribute"""


def add_attribute(objet, objname, value):
    """"Uses hasattr and setattr"""

    if hasattr(objet, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(objet, objname, value)
