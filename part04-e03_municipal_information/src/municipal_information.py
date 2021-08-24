#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv', sep= '\t')
    print("Shape: {}, {}".format(*df.shape))
    print("Columns:")
    for x in list(df.columns):
        print(x)

if __name__ == "__main__":
    main()
