# -*- coding: utf-8 -*-
"""

    Problem #53 - Combinatoric selections
    -------------------------------------

    There are exactly ten ways of selecting three from five, 12345:

        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5C3 = 10.

    In general,

               n!
    nCr =  ----------  where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
            r!(n−r)!

    It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
    
    How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
    greater than one-million?

"""

from math import factorial


def n_choose_r(n, r):
    """ Returns n choose r """

    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def problem_53():
    """ Attempt to solve the problem... """

    greater_than_million = 0
    for number in range(22, 101):
        for i in range(1, number + 1):
            if n_choose_r(n=number, r=i) >= 1000000:
                greater_than_million += 1

    return greater_than_million

if __name__ == "__main__":

    print('problem #53')
    ANSWER = problem_53()
    print('There are %s numbers greater than a million' % ANSWER)
