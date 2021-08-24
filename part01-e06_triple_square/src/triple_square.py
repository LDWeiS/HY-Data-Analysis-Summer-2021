#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        x = triple(i)
        y = square(i)

        if y > x:
            break
        
        print(f"triple({i})=={x} square({i})=={y}")

def square(x):
    return x**2

def triple(x):
    return x*3

if __name__ == "__main__":
    main()


