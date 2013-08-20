# -*- coding: utf-8 -*-
"""

    Problem #5 - Smallest multiple
    ------------------------------

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?

    Definitions:

    A multiple of a number is the product of that number and an integer.
    For example, 10 is a multiple of 5 because 5 * 2 = 10, so 10 is
    divisible by 5 and 2. Because 10 is the smallest positive integer that is
    divisible by both 5 and 2, it is the least common multiple of 5 and 2.

    By the same principle, 10 is the least common multiple of -5 and 2 as well.
    The following formula reduces the problem of computing the least common
    multiple to the problem of computing the greatest common divisor (GCD)::

        lcm(a, b) = abs(a*b)/gcd(a,b)

    GCD, implies: Euclidean algorithm (pseudo-code)::

        function gcd(a, b)
            while b != 0
               t := b
               b := a mod t
               a := t
            return a

"""
from math import fabs
# define the upper and lower bounds
lower_bound = 1
upper_bound = 20


def gcd(a, b):
    """ Returns greates commond denominator of a and b """

    while b:
        t = b
        b = a % t
        a = t
    return a


def lcm(a, b):
    """ Returns the lowest common multiple of a and b """

    return fabs(a*b)/gcd(a, b)


def problem():
    """ Attempt to solve the problem... """

    print 'problem #5'
    # +1 because of zero index
    num_range = range(lower_bound, upper_bound + 1)
    a = num_range.pop()
    b = num_range.pop()
    answer = lcm(a, b)
    # We can just continue to recalculate the lcm for each new number in the
    # list because: lcm(a,b,c) = lcm(a,lcm(b,c))
    for x in num_range:
        answer = lcm(x, answer)

    print 'the smallest positive number that is evenly divisible by all of '\
          'the numbers from %d to %d is: %d' % (lower_bound, upper_bound,
          answer)


if __name__ == "__main__":
    problem()
