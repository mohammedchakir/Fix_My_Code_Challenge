#!/usr/bin/python3
""" this script describe a class of square that calcul perimeter """

import math


class Square:
    """A class representing a square."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return 4 * self.width

    def __str__(self):
        """A string representation of the square."""
        return f"Width: {self.width}, Height: {self.height}"


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
