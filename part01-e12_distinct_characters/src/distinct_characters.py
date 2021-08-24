#!/usr/bin/env python3

def distinct_characters(L):
    newDict = {}

    for i in L:
        wordSet = set(i)
        newDict[i] = len(wordSet)

    return newDict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
