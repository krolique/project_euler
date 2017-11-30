# -*- coding: utf-8 -*-
"""

    Problem #33 - Digit canceling fractions
    ---------------------------------------

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #33'

    numerator = 1
    denominator = 1

    for a in xrange(10, 99):
        for b in xrange(10, 99):
            if a >= b or a % 10 == 0 or b % 10 == 0:
                continue
            r = a / float(b)
            i, j = str(a), str(b)
            if i[1] == j[0] and int(i[0]) / float(j[1]) == r:
                numerator *= int(i[0])
                denominator *= int(j[1])

    print 'denominator in lowest terms is: %s' % (denominator / numerator)

if __name__ == "__main__":

    problem()
