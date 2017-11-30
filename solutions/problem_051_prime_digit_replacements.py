# -*- coding: utf-8 -*-
"""

    Problem #51 - Prime digit replacements
    --------------------------------------

    By replacing the 1st digit of the 2-digit number *3, it turns out that six
    of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family:

        56003, 56113, 56333, 56443, 56663, 56773, and 56993.

    Consequently 56003, being the first member of this family, is the smallest
    prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight
    prime value family.

"""

from common import seive_generator


def problem_51():
    """ Attempt to solve the problem... """

    primes = list(seive_generator(999))
    for prime in primes:
        prime = str(prime)
        if len(prime) != 2:
            continue
        for x in xrange(0, 10):
            print 
        print prime

    return 0


if __name__ == "__main__":

    print 'problem #51'
    ANSWER = problem_51()
    print 'The smallest prime of the eight prime family is %s' % ANSWER
