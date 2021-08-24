#!/usr/bin/env python3
from functools import reduce
import numpy as np

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    else:
        gen = (a for i in range(abs(n)))
        fun = lambda x,y : x@y
        multiplicated = reduce(fun, gen)
        if n > 0:
            return multiplicated
        else:
            return np.linalg.inv(multiplicated)

def main():    
    np.random.seed(0)
    a=np.random.randint(0,10, (2,2))
    print(matrix_power(a, 3))


if __name__ == "__main__":
    main()
