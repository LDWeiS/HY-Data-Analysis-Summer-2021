#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    temp = L[0]
    rangeDetect = []
    detectList = []

    rangeDetect.append(temp)

    for i in range(1, len(L)):
        if (L[i] - temp != 1):
            if (len(rangeDetect) == 1):
                detectList.append(rangeDetect[0])
            
            else:
                detectList.append((rangeDetect[0], rangeDetect[-1] + 1))

            rangeDetect = []
        
        temp = L[i]
        rangeDetect.append(temp)

    if (len(rangeDetect) == 1):
                detectList.append(rangeDetect[0])
            
    else:
        detectList.append((rangeDetect[0], rangeDetect[-1] + 1))

    return detectList

def main():
    L = [2,5,4,8,12,6,7,10,13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
