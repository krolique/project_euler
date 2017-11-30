# -*- coding: utf-8 -*-
"""

    Problem #31 - Factorial digit sum
    ---------------------------------

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10!
    is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

"""
from operator import mul


def problem():
    """ Attempt to solve the problem... """

    print 'problem #20'

    digit_sum = sum(int(x) for x in str(reduce(mul, xrange(1, 100))))
    print 'the sum of the digits of 100! is: %d' % digit_sum


if __name__ == "__main__":

    problem()
