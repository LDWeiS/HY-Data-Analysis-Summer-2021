#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv('src/bands.tsv', sep= '\t')
    top40 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep= '\t')
    bands['Band'] = bands['Band'].str.upper()

    df = pd.merge(top40, bands, left_on=['Artist'], right_on=['Band'])

    print(df)

    return df

def main():
    top_bands()
    return

if __name__ == "__main__":
    main()
