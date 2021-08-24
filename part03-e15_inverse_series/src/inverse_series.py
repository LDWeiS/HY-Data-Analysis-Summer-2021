#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index.values, index=s)

def main():
    x = [1, 2, 3]
    y = ['a', 'b', 'c']
    xy = pd.Series(y, index = x)
    print(xy)
    yx = inverse_series(xy)
    print(yx)
    return

if __name__ == "__main__":
    main()
