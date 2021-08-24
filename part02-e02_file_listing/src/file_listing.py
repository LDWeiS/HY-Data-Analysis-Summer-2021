#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    res = []

    pattern = r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)'

    with open(filename, 'r') as f:
        for i in f:
            size, month, day, hour, minute, filename = re.search(expression, i).groups()
            res.append((int(size), month, int(day), int(hour), int(minute), filename))
            
    return res 

def main():
    file_listing()

if __name__ == "__main__":
    main()
