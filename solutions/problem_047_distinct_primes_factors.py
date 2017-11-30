# -*- coding: utf-8 -*-
"""

    Problem #47 - Distinct primes factors
    -------------------------------------

    The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors
    are:

        644 = 2^2 × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19

    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?

"""

from common import prime_number_list


def prime_facts(primes, number):
    """Returns a set of prime numbers """

    facts = set()
    sqr = number ** 0.5
    for prime in primes:
        if prime > sqr:
            if number > 1:
                facts.add(number)
            break
        while number % prime == 0:
            facts.add(prime)
            number /= prime
            sqr = number ** 0.5

    return facts


def problem_47():
    """ Attempt to solve the problem... """

    primes = prime_number_list(100000)

    consecutive = 0
    for number in xrange(640, 9999999):
        if len(prime_facts(primes, number)) == 4:
            consecutive += 1
            if consecutive == 4:
                # since the number we've reached here is the last number out
                # of the four we can just subtract 3 from it to know the first
                # number is the sequence
                return number - 3
        else:
            # reset the counter every time we don't find exactly 4 prime
            # factors
            consecutive = 0

if __name__ == "__main__":

    print 'problem #47'
    ANSWER = problem_47()
    print '%s' % ANSWER
