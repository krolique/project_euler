# -*- coding: utf-8 -*-
"""

    Problem #49 - Prime permutations
    --------------------------------

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways:

         (i) each of the three terms are prime
        (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?

"""

from math import fabs, log10

from common import seive_generator, permutations


def problem_49():
    """ Attempt to solve the problem... """

    # create a list of primes that are exactly 4 digits
    primes = [x for x in list(seive_generator(9999) )if int(log10(x)) + 1 == 4]
    know_seq = [1487, 4817, 8147]

    for x in primes:
        perms = set()
        
        for v in list(permutations(str(x))):
            prime = ''.join(v)
            if len(prime) is not 4:
                continue
            prime = int(prime)
            if prime in primes:
                perms.add(prime)


        maches = set()
        for y in perms:
            for z in perms:
                if fabs(y - z) == 3330:
                    maches.add(y)
        if len(maches) == 3:
            print x
            print maches



    return 0

if __name__ == "__main__":

    print 'problem #49'
    ANSWER = problem_49()
    print '%s' % ANSWER
