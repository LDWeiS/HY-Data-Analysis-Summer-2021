#!/usr/bin/env python3

def interleave(*lists):
    t = list(zip(*lists))
    flat_list = [item for sublist in t for item in sublist]
    return flat_list
    

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
