# Enter you module contents here

"""Triangles are hard. Use this module to guide you."""

from math import sqrt

__name__ = "triangle.py"
__version__ = '0.01'
__author__ = 'Nick5'

def hypothenuse(x, y):
    """Use this function to calculate the hypothenuse by providing the sides of a right angle triangle"""
    return sqrt(x**2 + y**2)

def area(x, y):
    """Use this function to calculate the area by providing the sides of a right angle triangle"""
    return x*y/2

# Define a class
class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def triangleInfo(self):
        print(f"This triangle has the width of {self.widht} and height of {self.height}")