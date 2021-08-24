#!/usr/bin/env python3

import numpy as np
from numpy.core.fromnumeric import shape
import scipy.linalg

def vector_angles(X, Y):
    xyProd = np.sum(X*Y, axis = 1)
    xNorm = scipy.linalg.norm(X, 2, axis = 1)
    yNorm = scipy.linalg.norm(Y, 2, axis = 1)

    xyDot = np.clip(xyProd/(xNorm * yNorm), -1.0, 1.0)
    return np.degrees(np.arccos(xyDot))

def main():
    np.random.seed(9)
    a=np.random.randint(0, 10, (2,2))
    b=np.random.randint(0, 10, (2,2))

    print(vector_angles(a,b))

if __name__ == "__main__":
    main()
