#!/usr/bin/env python3

def transform(s1, s2):
    if not s1 or not s2:
        return []

    return [ x * y for (x, y) in zip(map(int, s1.split(" ")), map(int, s2.split(" ")))]


    # L1 = map(int, s1.split(" "))
    # L2 = map(int, s2.split(" "))
    # product = []

    # for n1, n2 in zip(L1, L2):
    #     product.append(n1 * n2)

    # return product

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
