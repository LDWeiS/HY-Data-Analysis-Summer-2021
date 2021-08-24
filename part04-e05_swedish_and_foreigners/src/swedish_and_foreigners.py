#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df["Akaa":"Äänekoski"]
    cols = df.columns
    filtered = df[(df[cols[2]] > 5) & (df[cols[3]] > 5)]
    return filtered[[cols[0], cols[2], cols[3]]]

def main():
    df=swedish_and_foreigners()
    return

if __name__ == "__main__":
    main()
