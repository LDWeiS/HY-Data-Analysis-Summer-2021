#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    b = a[:,c] 
    _,s,t = np.unique(b, return_inverse=True, return_counts=True)
    idx = np.argsort(t[s])

    return a[idx][::-1]

def main():
    a = ([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
    [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
    [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
    [2, 3, 8, 1, 3, 3, 3, 7, 0, 1]])

    print(most_frequent_first(a, 0))

if __name__ == "__main__":
    main()
