# -*- coding: utf-8 -*-
"""

    Problem #7 - 10001st prime
    --------------------------

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10,001st prime number?

"""

from common import seive_generator


def problem_7():
    """ Attempt to solve the problem... """

    return [x for x in seive_generator(300000)][10000]


if __name__ == "__main__":

    print 'problem #7'
    ANSWER = problem_7()
    print 'The 10,001st prime number is: %d' % ANSWER
