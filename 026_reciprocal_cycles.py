# -*- coding: utf-8 -*-
"""

    Problem #26 - Reciprocal cycles
    -------------------------------

    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:

        1/2     =   0.5
        1/3     =   0.(3)
        1/4     =   0.25
        1/5     =   0.2
        1/6     =   0.1(6)
        1/7     =   0.(142857)
        1/8     =   0.125
        1/9     =   0.(1)
        1/10    =   0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.

"""


def cycles(n):
    """Return the length of the period for the cyclical number

    There is no general formula to find the period of a reciprocal, apart from
    checking whether the prime p divides some number 99...9. The idea here is
    to find the smallest `k` such that d/10^k-1. or 10*k % n = 1

    :param n: cyclical number
    :type n: int
    :returns: int
    """
    k = 1
    for i in xrange(1, n):
        k = 10 * k % n
        if k == 1:
            return i


def problem():
    """ Attempt to solve the problem... """

    print 'problem #26'

    # Terminating decimals represent rational numbers of the form k/(2^n5^m).
    # because of this fact the numbers that are coprime to 2 and 5 are skipped
    d = {cycles(i): i for i in xrange(2, 1000) if not i % 2 == 0
         and not i % 5 == 0}
    m = max(d)
    print 'longest recurring cycle is %s' % d[m]


if __name__ == "__main__":

    problem()
