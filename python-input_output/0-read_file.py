#!/usr/bin/python3
""" Contains a function that reads a text file """


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
