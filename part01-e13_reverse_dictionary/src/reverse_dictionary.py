# !/usr/bin/env python3
from collections import defaultdict

def reverse_dictionary(d):
    revDict = {}

    for k, v in d.items():

        for vItem in v:
            if vItem not in revDict.keys():
                revDict[vItem] = [k]

            else:
                revDict[vItem].append(k)
    
    return revDict

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)

if __name__ == "__main__":
    main()
