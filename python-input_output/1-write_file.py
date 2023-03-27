#!/usr/bin/python3
"""Function write_file()"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)
     and returns the number of characters written"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
