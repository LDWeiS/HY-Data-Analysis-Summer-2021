#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    num_list = []
    with open(filename, 'r') as f:
        for i in f:
            try:
                num_list.append(float(i))
            except:
                pass  
    sm = sum(num_list)
    av = statistics.mean(num_list)
    std = statistics.stdev(num_list)    
    return (sm, av, std)

def main():
    files = sys.argv[1:]
    for i in files:
        sm, av, std = summary(i)
        print(f"File: {i} Sum: {sm:.6f} Average: {av:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
