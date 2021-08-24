#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    a1, a2 = np.split(a, 2, axis=1)
    mask = np.sum(a1, axis=1) > np.sum(a2, axis=1)
    return a[mask]


def main():
    a = np.array([[2, 2, 1, 2],
              [1, 3, 4, 2]])

    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
