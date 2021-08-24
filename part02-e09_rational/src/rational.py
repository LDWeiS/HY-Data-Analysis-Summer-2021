#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return "Rational(%i, %i)" % (self.numerator, self.denominator)

    def __mul__(self, num):
        top = self.numerator.__mul__(num.numerator)
        bot = self.denominator.__mul__(num.denominator)

        return Rational(top, bot)
    
    def __truediv__(self, num):
        top = self.numerator.__mul__(num.denominator)
        bot = self.denominator.__mul__(num.numerator)

        return Rational(top, bot)
    
    def __add__(self, num):
        if self.denominator == num.denominator:
            top = self.numerator.__add__(num.numerator)
            bot = self.denominator
        else:
            top = self.numerator.__mul__(num.denominator) + num.numerator.__mul__(self.denominator)
            bot = self.denominator.__mul__(num.denominator)

        return Rational(top, bot)
    
    def __sub__(self, num):
        if self.denominator == num.denominator:
            top = self.numerator.__sub__(num.numerator)
            bot = self.denominator
        else:
            top = self.numerator.__mul__(num.denominator) - num.numerator.__mul__(self.denominator)
            bot = self.denominator.__mul__(num.denominator)

        return Rational(top, bot)

    def __eq__(self, num):
        num_1 = self.numerator.__mul__(num.denominator)
        num_2 = num.numerator.__mul__(self.denominator)

        return num_1 == num_2
    
    def __gt__(self, num):
        num_1 = self.numerator.__mul__(num.denominator)
        num_2 = num.numerator.__mul__(self.denominator)

        return num_1 > num_2
    
    def __lt__(self, num):
        num_1 = self.numerator.__mul__(num.denominator)
        num_2 = num.numerator.__mul__(self.denominator)

        return num_1 < num_2

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
