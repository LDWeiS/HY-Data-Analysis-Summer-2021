#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv')
    df['ratio'] = df['suicides_no']/df['population']
    fdata = df.groupby('country').mean()

    return fdata['ratio']

def main():
    suicide_fractions()
    return

if __name__ == "__main__":
    main()
