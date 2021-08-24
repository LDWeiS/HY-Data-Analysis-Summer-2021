#!/usr/bin/env python3

def find_matching(L, pattern):

    match = []

    for i, j in enumerate(L):
        if pattern in j:
            match.append(i)

    return match

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
