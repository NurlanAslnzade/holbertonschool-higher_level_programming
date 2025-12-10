#!/usr/bin/python3
"""Module that defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        return self.__height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__height + self.__width) * 2
        
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        siyahi = []
        for _ in range(self.__height):
            siyahi.append(self.__width * "#")
        return "\n".join(siyahi)
    
    def __repr__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
            siyahi = []
        for _ in range(self.__height):
            siyahi.append(self.__width * "#")
        return "\n".join(siyahi)
