#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """ Class that defines a Student object """

    def __init__(self, first_name, last_name, age):
        """ Class Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves Class dictionary """
        return self.__dict__.copy()
