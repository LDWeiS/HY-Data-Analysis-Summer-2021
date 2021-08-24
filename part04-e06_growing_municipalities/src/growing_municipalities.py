#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    m = (df["Population change from the previous year, %"] > 0.0)
    growing = df[m]
    percGrowth = growing.shape[0]/df.shape[0]
    return "{:.1f}".format(percGrowth)

def main():
    df = pd.read_csv("src/municipal.tsv", index_col=0, sep="\t")
    df = df["Akaa":"Äänekoski"]
    print(f"Proportion of growing municipalities: {growing_municipalities(df)}%")
    return

if __name__ == "__main__":
    main()
