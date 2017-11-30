# -*- coding: utf-8 -*-
"""

    Problem #37 - Truncatable primes
    --------------------------------

    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
    left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

from common import Seive


primes = {p: 1 for p in Seive(16000000)}


def problem():
    """ Attempt to solve the problem... """

    print 'problem #37'
    s = 0
    for n in primes:
        if n <= 7:
            continue
        p = str(n)
        truncatable_prime = True
        for i in xrange(1, len(p)):
            if int(p[:i]) not in primes or int(p[i:]) not in primes:
                truncatable_prime = False
                break
        if truncatable_prime:
            s += n

    print 'the sum of truncatable primes is: %s' % s


if __name__ == "__main__":

    problem()
