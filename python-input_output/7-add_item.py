#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then save them to a file"""
import sys

save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
try:
    new = load_json(file)
except (ValueError, FileNotFoundError):
    new = []
for args in sys.argv[1:]:
    new.append(args)
save_json(new, file)
