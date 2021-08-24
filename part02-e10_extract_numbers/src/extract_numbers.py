#!/usr/bin/env python3

def extract_numbers(s):
    numSplit = s.split()
    numReturn = []

    for word in numSplit:
        try:
            numReturn.append(int(word))
        except:
            try:
                numReturn.append(float(word))
            except:
                pass
    
    return numReturn

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
