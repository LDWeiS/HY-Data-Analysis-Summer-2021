#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    dfFreeze = df[df['Air temperature (degC)'] < 0]
    return dfFreeze['Air temperature (degC)'].count()

def main():
    freezer = below_zero()
    print(f"Number of days below zero: {freezer}")
    
if __name__ == "__main__":
    main()
