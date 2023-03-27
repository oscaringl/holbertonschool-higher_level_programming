#!/usr/bin/python3
"""Function load_from_json_file()"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="UTF8") as f:
        return json.loads(f.read())
