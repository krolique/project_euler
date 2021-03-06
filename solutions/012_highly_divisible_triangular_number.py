# -*- coding: utf-8 -*-
"""

    Problem #12 - Highly divisible triangular number
    ------------------------------------------------

    The sequence of triangle numbers is generated by adding the natural
    numbers. So the 7th triangle number would be:

        1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

    The first ten terms would be:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers::

         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred
    divisors?

"""
from math import sqrt

# maximum number of divisors to find
number_of_divisors = 500


def factors(n):
    """ Return a list factors of n """
    factors = []
    # For every exact divisor up to the square root, there is a corresponding
    # divisor above the square root.
    for x in range(1, int(sqrt(n) + 1)):
        if n % x == 0:
            factors.append(x)
            factors.append(n // x)
    return factors


def problem():
    """ Attempt to solve the problem... """

    print 'problem #12'
    n = 1
    while True:
        triangle_number = n*(n+1)/2
        n += 1
        if len(factors(triangle_number)) >= number_of_divisors:
            break

    print 'The first triangle number to have over %d divisors '\
          'is: %d' % (n, triangle_number)

if __name__ == "__main__":

    problem()
