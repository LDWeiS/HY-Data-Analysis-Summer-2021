#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    dfJuly = df[df['m'] == 7]
    return dfJuly["Air temperature (degC)"].mean()

def main():
    ave = average_temperature()
    print(f'Average temperature in July: {ave:.1f}')
    return

if __name__ == "__main__":
    main()
