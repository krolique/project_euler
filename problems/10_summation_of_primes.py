"""
    Problem 10
    ----------

    Summation of primes

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.

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
        #: Refinement: initially list odd numbers only, (3, 5, ..., n), and
        #: count up using an increment of 2p in step 3, thus marking only odd
        #: multiples of p greater than p itself. +1 to be inclusive
        self.seive = range(3, self.upper_bound+1, 2)
        #: compute the size
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

    print 'problem #10'
    total_prime_sum = 0
    for x in Seive(10000000):
        if x >= 2000000:
            break
        total_prime_sum += x
    print total_prime_sum


if __name__ == "__main__":

    problem()
