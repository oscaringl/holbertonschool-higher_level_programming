#!/usr/bin/python3
"""Contains class that inherits from list"""


class MyList(list):
    """Class inherits from list"""

    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))
