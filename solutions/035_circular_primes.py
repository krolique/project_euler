# -*- coding: utf-8 -*-
"""

    Problem #35 - Circular primes
    -----------------------------

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime. There are thirteen such
    primes below 100:

        2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

"""

from common import Seive


primes = {p: 1 for p in Seive(1000000)}


def circular_prime(n):
    """Return True or False if the a prime is circular """
    s = str(n)
    for i in xrange(len(s) - 1):
        s = s[1:] + s[0]
        if int(s) not in primes:
            return False
    return True


def problem():
    """ Attempt to solve the problem... """

    print 'problem #35'
    circular_primes = [n for n in primes if circular_prime(n)]

    print 'number of circular primes is: %s' % len(circular_primes)


if __name__ == "__main__":

    problem()
