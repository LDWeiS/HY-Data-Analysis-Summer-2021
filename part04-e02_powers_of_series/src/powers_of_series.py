#!/usr/bin/env python3

from numpy.lib.shape_base import column_stack
import pandas as pd

def powers_of_series(s, k):
    df = pd.DataFrame(s, columns = [1])

    for i in range(2, k+1):
        stemp = s**i
        df[i] = stemp

    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
