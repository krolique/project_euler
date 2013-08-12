# -*- coding: utf-8 -*-
"""

    Problem #3
    ----------

    Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?


    The fundamental theorem of arithmetic:

        Any positive integer can be divided in primes in essentially only one
        way. The phrase 'essentially one way' means that we do not consider
        the order of the factors important.

"""
from math import sqrt

# the number to factor
n = 600851475143


def factorization(n):
    """ Returns a list of factors of n.

    Biggest problem with this def is O(n^2)...
    """

    factors = []
    for i in xrange(2, int(sqrt(n))):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 1:
        factors.append(n)

    return factors


def problem():
    """ Attempt to solve the problem... """

    print 'problem #3'
    factors = factorization(n)
    print 'the largest prime factor of %d is: %d' % (n, max(factors))

if __name__ == "__main__":
    problem()
