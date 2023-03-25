#!/usr/bin/python3
"""Make the class MyInt"""


class MyInt(int):
    """Rebel version of an int"""
    def __eq__(self, other):
        """Returns the opposite of equal(eq)"""
        return int(self) != other

    def __ne__(self, other):
        """Returns the opposite of not equal(ne)"""
        return int(self) == other
