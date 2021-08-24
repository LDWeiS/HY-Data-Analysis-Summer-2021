#!/usr/bin/env python3

class Prepend(object):
    """Prepend class function to do something"""

    def __init__(self, name):
        """Adds a name to the object"""
        self.name = name

    def write(self, s):
        """This is print statement"""
        print(f"{self.name}{s}")
    # Add the methods of the class here

def main():
    p = Prepend("+++ ")
    p.write("Hello");

if __name__ == "__main__":
    main()
