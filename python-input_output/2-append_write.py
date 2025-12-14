#!/usr/bin/python3
"""append a text"""


def append_write(filename="", text=""):
    """appending text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
