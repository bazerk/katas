# -*- encoding: utf-8 -*-

"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

import itertools


PANDIGITAL = '123456789'


def problem38():
    largest = 0
    for i in xrange(1, 9999):
        digits = ''
        for n in itertools.count(1):
            digits += str(n * i)
            if len(digits) > 9:
                break
            if len(digits) == 9:
                if ''.join(sorted(digits)) == PANDIGITAL:
                    as_int = int(digits)
                    if as_int > largest:
                        largest = as_int
                    print '(%d, %d, %d)' % (i, n, as_int)
                break
    return largest


if __name__ == '__main__':
    print problem38()
