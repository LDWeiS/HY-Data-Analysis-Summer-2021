#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    r = '(\d+)\s+(\d+)\s+(\d+)\s+(.+)'

    with open(filename, mode="r")as f:
        rgbCode = re.findall(r, f.read())

    return [('\t').join(line) for line in rgbCode]

def main():
    red_green_blue()

if __name__ == "__main__":
    main()
