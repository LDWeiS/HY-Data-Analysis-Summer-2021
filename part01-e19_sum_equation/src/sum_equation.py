#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    
    lString = list(map(str, L))
    eq = " + ".join(lString)
    return(f"{eq} = {sum(L)}")

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
