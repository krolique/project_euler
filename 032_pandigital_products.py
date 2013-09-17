# -*- coding: utf-8 -*-
"""

    Problem #32 - Pandigital products
    ---------------------------------

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234,
    is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be sure to
    only include it once in your sum.

"""

from common import is_pandigital


def problem():
    """ Attempt to solve the problem... """

    print 'problem #32'

    pandigital = {}
    for a in xrange(1, 9999):
        for b in xrange(1, 999):
            p = a * b
            if pandigital.get(p) is None:
                m = '%s%s%s' % (a, b, p)
                if is_pandigital(m):
                    pandigital[p] = 0

    print 'the sum of 1-9 pandigitals is: %s' % str(sum(pandigital.keys()))


if __name__ == "__main__":

    problem()
