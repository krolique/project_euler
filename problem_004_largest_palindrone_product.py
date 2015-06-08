# -*- coding: utf-8 -*-
"""

    Problem #4 - Largest palindrome product
    ---------------------------------------

    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

"""

def problem_4():
    """ Attempt to solve the problem... """

    biggest = 0
    for i in xrange(100, 999):
        for j in xrange(100, 999):
            product = i*j
            if str(product) == str(product)[::-1] and product > biggest:
                biggest = product

    return biggest

if __name__ == "__main__":

    print 'problem #4'
    ANSWER = problem_4()
    print 'the biggest palindrome of 3-digit product is %d' % ANSWER
