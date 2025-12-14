#!/usr/bin/python3
"""using JSON represantion"""
import json as j


def save_to_json_file(my_obj, filename):
    """JSON represantion"""
    with open(filename, "w") as f:
        j.dump(my_obj, f)
