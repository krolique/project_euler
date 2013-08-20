# -*- coding: utf-8 -*-
"""

    Problem #14 - Longest Collatz sequence
    --------------------------------------

    The following iterative sequence is defined for the set of positive
    integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz_sequence(n):
    """Return collats sequence generator

    The Collatz conjecture is a conjecture in mathematics named after Lothar
    Collatz, who first proposed it in 1937. The conjecture is also known as
    the 3n + 1 conjecture, the Ulam conjecture (after Stanislaw Ulam),
    Kakutani's problem (after Shizuo Kakutani), the Thwaites conjecture
    (after Sir Bryan Thwaites), Hasse's algorithm (after Helmut Hasse), or
    the Syracuse problem;[1] the sequence of numbers involved is referred to
    as the hailstone sequence or hailstone numbers (because the values are
    usually subject to multiple descents and ascents like hailstones in a
    cloud) or as wondrous numbers.

    Take any natural number n. If n is even, divide it by 2 to get n / 2.
    If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the
    process (which has been called "Half Or Triple Plus One", or HOTPO[5])
    indefinitely. The conjecture is that no matter what number you start with,
    you shall always eventually reach 1. The property has also been called
    oneness.

    Paul Erdős said, allegedly, about the Collatz conjecture: "Mathematics is
    not yet ripe for such problems"[7] and also offered $500 for its solution.

    ..seemore:
        `Collatz conjecture <http://en.wikipedia.org/wiki/Collatz_conjecture>`_

    :param n: the starting point of the sequence
    :type n: int
    :returns: generator
    """

    yield n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        yield n


def problem():
    """ Attempt to solve the problem... """

    print 'problem #14'
    n = 0
    max_len = 0
    for i in xrange(1, int(1e6)+1):
        sequence_len = len([x for x in collatz_sequence(i)])
        if sequence_len > max_len:
            max_len, n = sequence_len, i

    print 'the starting number below 1,000,000 with the longest sequence '\
          'is: %d' % n


if __name__ == "__main__":

    problem()
