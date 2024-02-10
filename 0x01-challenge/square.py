#!/usr/bin/python3
""" this script describe a class of square that calcul perimeter """
import math


class Square():
    """ A class representing a square. """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Square class initialized """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """A string representation of the square."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Creating a Square instance """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
