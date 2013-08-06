# -*- coding: utf-8 -*-
"""

    Problem 7
    =========

    10001st prime

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10,001st prime number?


    Algorithm description
    ---------------------

        A prime number is a natural number which has exactly two distinct
        natural number divisors: 1 and itself. (0 is not a prime because it
        has many divisors and 1 is not a prime because it has only one divisor
        [debated, but whatever]).


        To find all the prime numbers less than or equal to a given integer n
        by Eratosthenes' method:

            1. Create a list of consecutive integers from 2 to n: (2, 3, 4,
                ..., n).

            2. Initially, let p equal 2, the first prime number.

            3. Starting from p, count up in increments of p and mark each of
               these numbers greater than p itself in the list. These will be
               multiples of p: 2p, 3p, 4p, etc.; note that some of them may
               have already been marked.

            4. Find the first number greater than p in the list that is not
               marked. If there was no such number, stop. Otherwise, let p
               now equal this number (which is the next prime), and repeat
               from step 3.

        Source: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

"""
from math import sqrt


class Seive(object):
    """ Prime Number Seive """

    def __init__(self, upper_bound=0):
        """ """

        self.upper_bound = upper_bound
        self.seive = []
        self.eratosthenes_seive()

    def eratosthenes_seive(self):
        """ Returns prime numbers upto the number n using the sieve of
        eratosthenes method.

        """
        # Refinement: initially list odd numbers only, (3, 5, ..., n), and count
        # up using an increment of 2p in step 3, thus marking only odd multiples
        # of p greater than p itself. +1 to be inclusive
        self.seive = range(3, self.upper_bound+1, 2)
        # compute the size
        size = len(self.seive)
        i = 0
        while i <= sqrt(self.upper_bound):
            if self.seive[i]:
                for x in xrange(i + self.seive[i], size, self.seive[i]):
                    self.seive[x] = 0
            i += 1

    def __iter__(self):
        """ """

        if self.upper_bound > 1:
            yield 2

        for x in self.seive:
            if x:
                yield x


def problem():
    """ Attempt to solve the problem... """

    print 'problem #7'
    # perhaps a generator would be most useful here for finding primes
    # but the most economical way would be to use sieve of eratosthenes
    # so we're going to have to generate enough primes to pass the 10,001
    # mark.
    s1 = Seive(300000)
    primes = [x for x in s1]
    print 'The 10,001st prime number is: %d' % primes[10000]


if __name__ == "__main__":
    problem()
