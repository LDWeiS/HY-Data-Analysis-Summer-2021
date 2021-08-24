#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(painting):
    grey = [0.2126, 0.7152, 0.0722]
    painting2 = painting.copy()    # don't mess the original painting!
    toGrey = np.sum(painting2 * grey, axis = 2)
    return toGrey

def to_red(painting):
    multiplicators = [1, 0, 0]
    return painting * multiplicators

def to_green(painting):
    multiplicators = [0, 1, 0]
    return painting * multiplicators

def to_blue(painting):
    multiplicators = [0, 0, 1]
    return painting * multiplicators

def main():
    painting=plt.imread('src/painting.png')
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting)) 
    ax[2].imshow(to_blue(painting))
    plt.show()

    toGrey = to_grayscale(painting)
    plt.imshow(toGrey)
    plt.gray()
    plt.show()

if __name__ == "__main__":
    main()
