# -*- coding: utf-8 -*-
"""

    Problem #21 - Amicable numbers
    ------------------------------

    Let d(n) be defined as the sum of proper divisors of n (numbers less than
    n which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
    and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are

        1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;

    therefore d(220) = 284. The proper divisors of 284 are

        1, 2, 4, 71 and 142;

    so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #21'

    d = lambda x: sum(y for y in xrange(1, x) if x % y == 0)

    t = 0
    for a in xrange(1, 10000):
        b = d(a)
        if b != a and a == d(b):
            t += a
            print a
    print 'the sum of amicable numbers is %s' % t

if __name__ == "__main__":

    problem()
