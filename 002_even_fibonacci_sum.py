# -*- coding: utf-8 -*-
"""

    Problem #2 - Even Fibonacci numbers
    -----------------------------------

    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be::

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
"""

from common import fib_generator


def problem():
    """ Attempt to solve the problem... """

    print 'problem #2'
    upper_bound = 4 * 10**6
    gen = fib_generator()
    total = 0
    while True:
        num, i = gen.next()
        if num >= upper_bound:
            break
        #: only even
        if num % 2 == 0:
            total += num
    print 'sum of even fibonacci numbers less than 4e6 is: %d ' % total

if __name__ == "__main__":

    problem()
