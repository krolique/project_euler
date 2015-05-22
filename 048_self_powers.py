# -*- coding: utf-8 -*-
"""

    Problem #48 - Self powers
    -------------------------

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #48'
    digits = str(sum(x**x for x in range(1, 1001)))[-10:]
    print 'the sum of last ten digits are %s' % digits

if __name__ == "__main__":

    problem()
