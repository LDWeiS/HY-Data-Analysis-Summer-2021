#!/usr/bin/env python3

def merge(L1, L2):
    newList = []
    i, j = 0, 0

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            newList.append(L1[i])
            i += 1
        else:
            newList.append(L2[j])
            j += 1

    newList = newList + L1[i:] + L2[j:]

    return newList

def main():
    L = merge([1, 5, 9, 12], [2, 6, 10])
    print(L)

if __name__ == "__main__":
    main()
