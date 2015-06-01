# -*- coding: utf-8 -*-
"""

    Problem #3 - Largest prime factor
    ---------------------------------

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?


    The fundamental theorem of arithmetic
    -------------------------------------
    Any positive integer can be divided in primes in essentially only one
    way. The phrase 'essentially one way' means that we do not consider
    the order of the factors important.

"""

from common import simple_factorization


def problem_3():
    """ Attempt to solve the problem... """

    factors = simple_factorization(600851475143)
    return max(factors)

if __name__ == "__main__":

    print 'problem #3'
    ANSWER = problem_3()
    print 'the largest prime factor of 600851475143 is: %d' % ANSWER
