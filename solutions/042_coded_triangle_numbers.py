# -*- coding: utf-8 -*-
"""

    Problem #42 - Coded triangle numbers
    ------------------------------------

    The n-th term of the sequence of triangle numbers is given by:

        t(n) = n*(n+1)/2;

    so the first ten triangle numbers are:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Using words.txt a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #42'
    t_inv = lambda x: int(((1+8*x)**(0.5) - 1) / 2)
    t = lambda x: x*(x+1)/2

    with open('042_words.txt', 'r') as f:
        words = [x.replace('"', '').lower() for x in f.read().split(',')]
        sums = [sum(ord(i) - 96 for i in x) for x in words]
        triangle_words = sum(1 for x in sums if x == t(t_inv(x)))
        print 'the number of triable words in the file is: %s' % triangle_words


if __name__ == "__main__":

    problem()
