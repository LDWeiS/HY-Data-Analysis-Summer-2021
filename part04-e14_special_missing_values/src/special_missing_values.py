#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pandas.core.arrays.integer import Int64Dtype

def special_missing_values():
    pd.set_option('display.max_rows', None)
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    df = df.replace(['New', 'Re'], np.nan).dropna()
    df["LW"] = pd.to_numeric(df["LW"])

    return df[df['Pos'] > df['LW']]

def main():
    data = special_missing_values()
    print(data)

if __name__ == "__main__":
    main()
