# -*- encoding: utf-8 -*-

"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

divisors = [13, 11, 7, 5, 3, 2]


def _find_valid(value, level):
    if level >= len(divisors):
        for i in range(1, 10):
            if str(i) not in value:
                yield str(i) + value
        return
    base = value[:2]
    divisor = divisors[level]
    for i in range(0, 10):
        if str(i) not in value:
            tst = str(i) + base
            if int(tst) % divisor == 0:
                new_value = str(i) + value
                for v in _find_valid(new_value, level + 1):
                    yield v


def problem43():
    total = 0
    for ix in itertools.count(1):
        d8d9d10 = ix * 17
        if d8d9d10 >= 1000:
            break
        as_str = '%03d' % d8d9d10
        check = set()
        valid = True
        for ch in as_str:
            if ch in check:
                valid = False
            check.add(ch)
        if valid:
            for value in _find_valid(as_str, 0):
                print value
                total += int(value)
    return total


if __name__ == '__main__':
    print problem43()
