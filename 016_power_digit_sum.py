# -*- coding: utf-8 -*-
"""

    Problem #16 - Power digit sum
    -----------------------------

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?

"""

def problem():
    """ Attempt to solve the problem... """

    print 'problem #16'
    print 'the sum of 2^1000 digits is %s' % sum(int(x) for x in str(2**1000))    


if __name__ == "__main__":

    problem()
