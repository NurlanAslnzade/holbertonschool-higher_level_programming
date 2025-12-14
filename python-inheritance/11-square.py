#!/usr/bin/python3
"""nese"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """nese"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return super().area()

    return "[Square] {}/{}".format(
    self._Rectangle__width, self._Rectangle__height
)
