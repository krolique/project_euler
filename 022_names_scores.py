# -*- coding: utf-8 -*-
"""

    Problem #22 - Names scores
    --------------------------

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text
    file containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?

"""


def problem():
    """ Attempt to solve the problem... """

    print 'problem #22'

    names = []
    with open('names.txt') as f:
        for line in f:
            names.extend([x.replace('"', '') for x in line.split(',')])

    t = 0
    i = 1
    for n in sorted(names):
        t += i * sum((ord(x) - 64) for x in n)
        i += 1

    print 'the sum of all scores in the file is: %s' % t


if __name__ == "__main__":

    problem()
