#!/usr/bin/python3
'''
A module providing utilities for handling fractions
'''


def get_gcd(num_1, num_2):
    '''
    Returns the greatest common denominator
    between two numbers
    '''
    if num_1 % num_2 == 0:
        return num_2
    else:
        return get_gcd(num_2, num_1 % num_2)


class Fraction:
    """
    A simple class for manipulating and viewing fractions
    """

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        if self.num == self.den:
            return str(1)
        else:
            return str("%s/%s" % (self.num, self.den))

    def __add__(self, other_fraction):

        if isinstance(other_fraction, int):
            other_fraction = Fraction(other_fraction, 1)

        new_num = self.num * other_fraction.den + other_fraction.num * self.den
        new_den = self.den * other_fraction.den

        gcd = get_gcd(new_num, new_den)

        return Fraction(new_num // gcd, new_den // gcd)

    def __eq__(self, other_fraction):
        self.simplify()
        other_fraction.simplify()
        return True if self.num == other_fraction.num and self.den == other_fraction.den else False

    def simplify(self):
        '''
        Simplifies the fraction
        '''
        gcd = get_gcd(self.num, self.den)
        self.num = self.num // gcd
        self.den = self.den // gcd


def main():
    '''
    Tests class out
    '''

    f_1 = Fraction(3, 4)
    f_2 = Fraction(1, 4)
    f_3 = Fraction(5, 20)
    f_4 = Fraction(15, 20)

    print(f_1 == f_2)
    print(f_3)
    f_3.simplify()
    print(f_3)
    print(f_1 + 1)
    print(f_1 + f_2)
    print(f_1 == f_4)


if __name__ == "__main__":
    main()
