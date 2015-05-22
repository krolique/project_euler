# -*- coding: utf-8 -*-
"""

    Problem #44 - Pentagon numbers
    ------------------------------

    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first
    ten pentagonal numbers are:

        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
    70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
    difference are pentagonal and D = |Pk − Pj| is minimised; what is the
    value of D?

"""

def pentagonal():
    """ """

    i = 0
    while True:
        yield i, i*(3*i-1)/2
        i += 1

def problem():
    """ Attempt to solve the problem... """

    print 'problem #44'
    numbers = []
    p = pentagonal()
    for x in xrange(100):
        numbers.append(p.next())



if __name__ == "__main__":

    problem()
