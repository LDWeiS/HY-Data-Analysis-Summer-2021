#!/usr/bin/env python3
from os import read
import pandas as pd

def read_series():
    index = []
    values = []

    while True:
        dataIn = input("Enter data value: ")
        if len(dataIn) == 0:
            break
        else:
            lineSplit = dataIn.split()
            if len(lineSplit) < 2:
                raise Exception
            else:
                index.append(lineSplit[0])
                values.append(lineSplit[1])

    return pd.Series(values, index = index)

def main():
    read_series()

if __name__ == "__main__":
    main()
