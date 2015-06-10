# -*- coding: utf-8 -*-
"""

    Problem #46 - Goldbach's other conjecture
    -----------------------------------------

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

        9  = 7  + 2 * 1^2
        15 = 7  + 2 * 2^2
        21 = 3  + 2 * 3^2
        25 = 7  + 2 * 3^2
        27 = 19 + 2 * 2^2
        33 = 31 + 2 * 1^2

        sqrt(x - prime/2) = n

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?

"""

from math import sqrt

from common import seive_generator


def problem_46():
    """ Attempt to solve the problem... """

    primes = {x: 0 for x in seive_generator(10000)}
    for odd_number in xrange(9, 10000, 2):
        if primes.get(odd_number):
            continue
        is_goldbach = False
        for prime in primes.keys():
            if prime > odd_number:
                continue
            if sqrt((odd_number - prime) / 2.0) % 1 == 0:
                is_goldbach = True
                break
        if not is_goldbach:
            return odd_number

if __name__ == "__main__":

    print 'problem #46'
    ANSWER = problem_46()
    print 'the smallest odd composite that cannot be written as the sum of a'\
          ' prime and twice a square: %s' % ANSWER
