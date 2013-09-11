# -*- coding: utf-8 -*-
"""

    Problem #23 - Non-abundant sums
    -------------------------------

    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers
    is 24. By mathematical analysis, it can be shown that all integers greater
    than 28123 can be written as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though
    it is known that the greatest number that cannot be expressed as the sum
    of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.

"""

from common import proper_divisors


def problem():
    """ Attempt to solve the problem... """

    print 'problem #23'
    s = 0
    abundant_numbers = {}
    for x in xrange(1, 28123):
        d = proper_divisors(x)
        if sum(d) > x:
            abundant_numbers[x] = 0

        is_sum_found = False
        for i in abundant_numbers.keys():
            if abundant_numbers.get(x - i) is not None:
                is_sum_found = True
                break
        if not is_sum_found:
            s += x

    print 'the sum of all integers which cannot be written as the sum of two'\
          ' abundant numbers is %s' % s


if __name__ == "__main__":

    problem()
