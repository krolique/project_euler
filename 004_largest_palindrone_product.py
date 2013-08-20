# -*- coding: utf-8 -*-
"""

    Problem #4
    ----------

    Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

"""

# palindrome size
n = 3


def problem(n=n):
    """ Attempt to solve the problem... """

    print 'problem #4'
    biggest = 0
    for i in xrange(10**n):
        for j in xrange(10**n):
            product = i*j
            if str(product) == str(product)[::-1] and product > biggest:
                biggest = product

    print 'the biggest palindrome of %d-digit product is %d' % (n, biggest)

if __name__ == "__main__":
    problem()
