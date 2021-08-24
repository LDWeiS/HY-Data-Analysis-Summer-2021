#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    top40 = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep = '\t')
    goodness = top40.groupby("Publisher").sum()
    top = goodness['WoC'].idxmax()
    final_df = top40[top40['Publisher'] == top]

    print(goodness)
    print(top)

    return final_df

def main():
    df = best_record_company()
    return
    

if __name__ == "__main__":
    main()
