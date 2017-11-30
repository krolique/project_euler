# -*- coding: utf-8 -*-
"""

    Problem #34 - Digit factorials
    ------------------------------

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

from math import factorial


def problem():
    """ Attempt to solve the problem... """

    print 'problem #34'

    s = 0
    for n in xrange(3, 99999):
        if sum(factorial(int(c)) for c in str(n)) == n:
            s += n

    print 'the sum of all number is: %s' % s


if __name__ == "__main__":

    problem()
