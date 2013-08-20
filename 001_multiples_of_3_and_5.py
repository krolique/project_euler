# -*- coding: utf-8 -*-
"""
    Problem #1 - Multiples of 3 and 5
    =================================

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
    all the multiples of 3 or 5 below 1000.

    Solution
    --------

    Use :meth:`xrange` with upper bound of 1000 in list comprehension output
    from which will be passed to sum. The list comprehension will limit values
    in :meth:`xrange` with the following condition::

        if x %3 == 0 or x % 5 == 0

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #1'
    upper_bound = 1000
    total_sum = sum([x for x in xrange(upper_bound)
                    if x % 3 == 0 or x % 5 == 0])
    print 'sum of all multiple of 3 or 5 is: %d ' % total_sum

if __name__ == "__main__":

    problem()
