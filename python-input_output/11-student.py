#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Class that defines a Student object"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves Class dictionary base on attr
        If attr is a list of strings, only attributes contained in that list
        will be retrieved
        Otherwise all  attributes will be retrieved."""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload data from json"""
        for (key, value) in json.items():
            setattr(self, key, value)
