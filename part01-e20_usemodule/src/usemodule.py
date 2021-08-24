#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    x = triangle.area(1,2)
    y = triangle.hypothenuse(1,2)
    print(x, y)# Call the functions from here

if __name__ == "__main__":
    main()
