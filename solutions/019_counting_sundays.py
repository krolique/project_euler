# -*- coding: utf-8 -*-
"""

    Problem #19 - Counting Sundays
    ------------------------------

    You are given the following information, but you may prefer to do some
    research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

"""


def days(month, year):
    """Return the number of days in a month for a given year

    :param month: desired month
    :type month: int
    :param year: desired year
    :type year: int
    :returns: int
    """

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month == 2:
        if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 30


def problem():
    """ Attempt to solve the problem... """

    print 'problem #19'
    sundays = 0
    # Jan 1, 1901 was a Tuesday because, 1900 had 365 days and 364 % 7 = 1
    # which places Jan 01, 1901 as the next weekday after Monday :)
    weekday = 2
    for y in xrange(1901, 2001):
        for m in xrange(1, 13):
            if weekday == 0:
                sundays += 1
            weekday = (weekday + (days(m, y) % 7)) % 7

    print 'sundays that fell on the 1st of the month is: %s' % sundays


if __name__ == "__main__":

    problem()
