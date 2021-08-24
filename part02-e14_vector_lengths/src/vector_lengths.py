#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.power(a, 2).sum(axis = 1))

def main():
    b=np.array([[1,2,3], [4,5,6]])
    print(vector_lengths(b))

if __name__ == "__main__":
    main()
