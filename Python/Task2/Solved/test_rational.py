import unittest
import math
from rational import Rational
class Testing(unittest.TestCase):
    def test_add(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 6)
        expected_numerator = r1.numerator * r2.denominator + r2.numerator * r1.denominator
        expected_denominator = r1.denominator * r2.denominator
        result = r1.add(r2)

        self.assertEqual(result.numerator, expected_numerator) # calculates if the result gives what we expect
        self.assertEqual(result.denominator, expected_denominator)
    def test_subtract(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 6)
        result = r1.sub(r2)
        expected_numerator = (r1.numerator * r2.denominator - r1.denominator * r2.numerator)
        expected_denominator = (r1.denominator * r2.denominator)
        self.assertEqual(result.numerator, expected_numerator)
        self.assertEqual(result.denominator, expected_denominator)
    def test_mul(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 6)
        result = r1.mul(r2)
        expected_numerator = r1.numerator * r2.numerator
        expected_denominator = r1.denominator * r2.denominator
        self.assertEqual(result.numerator, expected_numerator)
        self.assertEqual(result.denominator, expected_denominator)
    def test_div(self):
        r1 = Rational(1, 4)
        r2 = Rational(2, 6)
        result = r1.div(r2)
        expected_numerator = r1.numerator * r2.denominator
        expected_denominator = r1.denominator * r2.numerator
        self.assertEqual(result.numerator, expected_numerator)
        self.assertEqual(result.denominator, expected_denominator)
    def test_invert(self):
        r = Rational(1, 4)
        inverted = r.invert()
        expected_numerator = r.denominator
        expected_denominator = r.numerator

        self.assertEqual(inverted.numerator, expected_numerator)
        self.assertEqual(inverted.denominator, expected_denominator)
    def test_negate(self):
        r1 = Rational(4, 8) # test with positive numerator
        negate = r1.negate()
        expected_numerator = -r1.numerator
        expected_denominator = r1.denominator
        self.assertEqual(negate.numerator, expected_numerator)
        self.assertEqual(negate.denominator, expected_denominator)
        r2 = Rational(-4, 8) # test with negative numerator
        negate = r2.negate()
        expected_numerator = -r2.numerator
        expected_denominator = r2.denominator
        self.assertEqual(negate.numerator, expected_numerator)
        self.assertEqual(negate.denominator, expected_denominator)
        r3 = Rational(0, 8) # test with numerator being 0
        negate = r3.negate()
        expected_numerator = -r3.numerator
        expected_denominator = r3.denominator
        self.assertEqual(negate.numerator, expected_numerator)
        self.assertEqual(negate.denominator, expected_denominator)
    def test_reduce(self):
        r = Rational(4, 16)
        reduced = r.reduce()
        gcd = math.gcd(r.numerator, r.denominator)
        expected_numerator = r.numerator // gcd
        expected_denominator = r.denominator // gcd

        self.assertEqual(reduced.numerator, expected_numerator)
        self.assertEqual(reduced.denominator, expected_denominator)
    def test_cmp_greater(self):
        r1 = Rational(5, 15)
        r2 = Rational(8, 40)
        result = r1.cmp(r2)
        self.assertEqual(result, 1)
    def test_cmp_equal(self):
        r1 = Rational(6, 24)
        r2 = Rational(1, 4)
        result = r1.cmp(r2)
        self.assertEqual(result, 0)
    def test_cmp_lesser(self):
        r1 = Rational(2, 6)
        r2 = Rational(3, 5)
        result = r1.cmp(r2)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()