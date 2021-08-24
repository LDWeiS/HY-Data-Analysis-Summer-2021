#!/usr/bin/env python3

import math

def triangle():
    base = float(input("Give the base of the triangle: "))
    height = float(input("Give the base of the triangle: "))
    return base*height/2

def rectangle():
    width = float(input("Give the width of the rectangle: "))
    height = float(input("Give the base of the rectangle: "))
    return width*height

def circle():
    radius = float(input("Give the radius of the circle: "))
    return math.pi*(radius**2)

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        
        if shape == "triangle":
            output = f"The area is {triangle():.5f}"
        elif shape == "rectangle":
            output = f"The area is {rectangle():.5f}"
        elif shape == "circle":
            output = f"The area is {circle():.5f}"
        elif shape == "":
            break
        else:
            output = "Unknown shape!"

        print(output)

if __name__ == "__main__":
    main()
