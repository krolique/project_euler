# -*- coding: utf-8 -*-
"""

    Problem #40 - Champernowne's constant
    -------------------------------------

    An irrational decimal fraction is created by concatenating the positive
    integers:

        0.123456789101112131415161718192021...
                     -

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of
    the following expression.

        d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #40'
    c = ''.join([str(x) for x in xrange(1, 10**6 + 1)])
    print reduce(lambda x, y: x * y, [int(c[10**x - 1]) for x in xrange(0, 7)])


if __name__ == "__main__":

    problem()
