#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pandas.core.arrays.categorical import contains

def clean_name(nameList):
    for i, line in enumerate(nameList):
        if ',' in line:
            name = line.replace(",","").split(' ')
            nameList[i] = name[1].title() + ' ' + name[0].title()
        else:
            name = line.split(' ')
            nameList[i] = name[0].title() + ' ' + name[1].title()

    return nameList

def clean_year(yearList):
    for i, line in enumerate(yearList):
        if line == '-':
            yearList[i] = None
        elif len(line) > 1:
            year = line.split(' ')
            yearList[i] = year[0]
    return yearList

def clean_seasons(seasonList):
    term = {'one':1, 'two':2}
    return seasonList.replace(term, value = None)

def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep = '\t')
    df['President'] = clean_name(df['President'])
    df['Vice-president'] = clean_name(df['Vice-president'])
    df['Start'] = clean_year(df['Start']).astype(int)
    df['Last'] = clean_year(df['Last']).astype(float)
    df['Seasons'] = clean_seasons(df['Seasons']).astype(int)

    # df.set_index('President', inplace= True)
    return df

def main():
    data = cleaning_data()
    # print(data)

if __name__ == "__main__":
    main()
