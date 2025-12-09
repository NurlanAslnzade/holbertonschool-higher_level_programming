#!/usr/bin/python3

class Rectangle:
    
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    
    @property
    def (self, width):
        return self.__width
        
    @width.setter
    def (self, width):
        if is not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueErrro("width must be >= 0")
        self.__width = width
        
    @property
    def (self, height):
        return self.__height
        
    @height.setter
    def (self, height):
        if is not isinstance(height, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueErrro("width must be >= 0")
        self.__height = height
