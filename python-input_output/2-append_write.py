#!/usr/bin/python3
"""Contains append_file() function"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8)
     and returns the number of characters written"""

    with open(filename, mode="a", encoding='utf-8') as my_file:
        return(my_file.write(text))
