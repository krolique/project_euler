# -*- coding: utf-8 -*-
"""

    Problem #50 - Consecutive prime sum
    -----------------------------------

    The prime 41, can be written as the sum of six consecutive primes:

        41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below
    one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?

"""

from common import seive_generator, subarray_sum


def problem_50():
    """ Attempt to solve the problem... """

    primes = list(seive_generator(1000000))
    best = (0, 0)
    for prime in primes:
        ans = subarray_sum(primes[:int(prime ** 0.5)], prime)
        if len(ans) > best[1]:
            best = (prime, len(ans))
    return best[0]


if __name__ == "__main__":

    print 'problem #50'
    ANSWER = problem_50()
    print 'Prime below one-million with the most consecutive sum '\
            'is %s' % ANSWER
