#!/usr/bin/python3
"""Function Defines "Student" class"""


class Student:
    """Student """
    def __init__(self, first_name, last_name, age):
        """Initializes student's information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation of
        Student instance"""
        return self.__dict__
