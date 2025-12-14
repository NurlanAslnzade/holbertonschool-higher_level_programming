#!/usr/bin/python3
"""loading JSON represantion"""
import json as j


def load_from_json_file(filename):
    """load JSON"""
    with open(filename) as f:
        return j.load(f)
