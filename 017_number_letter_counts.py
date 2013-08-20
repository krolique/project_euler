# -*- coding: utf-8 -*-
"""

    Problem #17 - Number letter counts
    ----------------------------------

    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.

"""

m = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    1000: 'one thousand'
}

n = 1000


def to_english(n):
    """Return the english representation of the number """

    try:
        return m[n]
    except KeyError:
        if n > 100:
            if n % 100:
                return '%s hundred and %s' % (m[n / 100], to_english(n % 100))
            else:
                return '%s hundred' % (m[n / 100])
        if n > 10:
            return '%s-%s' % (m[n-(n % 10)], m[n % 10])
        else:
            return m[n-(n % 10)]


def problem():
    """ Attempt to solve the problem... """

    print 'problem #17'
    digit_sum = sum(len(to_english(x).replace('-', '').replace(' ', '')) for x
                    in xrange(1, n+1))
    print 'The number of letters used is %s' % digit_sum

if __name__ == "__main__":

    problem()
