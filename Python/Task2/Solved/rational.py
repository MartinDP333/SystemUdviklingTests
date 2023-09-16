import math

class Rational():
    def __init__(self, numerator, denominator=1): # denominator is 1 if not set
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Rational(new_numerator, common_denominator)

    def sub(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        return Rational(new_numerator, common_denominator)

    def mul(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def div(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def invert(self):
        return Rational(self.denominator, self.numerator)

    def negate(self):
        return Rational(-self.numerator, self.denominator)

    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        reduced_numerator = self.numerator // gcd
        reduced_denominator = self.denominator // gcd
        return Rational(reduced_numerator, reduced_denominator)

    def cmp(self, other):
        if self.numerator * other.denominator > other.numerator * self.denominator:
            return 1
        elif self.numerator * other.denominator < other.numerator * self.denominator:
            return -1
        else:
            return 0
