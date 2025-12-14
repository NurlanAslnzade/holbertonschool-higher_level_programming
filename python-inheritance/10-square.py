#!/usr/bin/python3
"""nese olsun"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """sadasd"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self._Rectangle__width ** 2
