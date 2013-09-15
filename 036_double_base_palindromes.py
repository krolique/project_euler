# -*- coding: utf-8 -*-
"""

    Problem #36 - Double-base palindromes
    -------------------------------------

    The decimal number, 585 = 10010010012 (binary), is palindromic in both
    bases.

    Find the sum of all numbers, less than one million, which are palindromic
    in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include
    leading zeros.)

"""


def is_palindrone(n):
    """Returns True of the number or string is palindromic """
    n = str(n)
    return n == n[::-1]


def problem():
    """ Attempt to solve the problem... """

    print 'problem #36'

    s = 0
    for n in xrange(1, 10**6):
        if is_palindrone(n) and is_palindrone(bin(n)[2:]):
            s += n

    print 'the sum of palindromic numbers is: %s' % s


if __name__ == "__main__":

    problem()
