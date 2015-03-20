# -*- encoding: utf-8 -*-

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

import itertools


def problem40():
    fractional = ''
    for x in itertools.count(1):
        fractional += str(x)
        if len(fractional) >= 1000000:
            break

    total = 1
    for index in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        total *= int(fractional[index-1])
    return total


if __name__ == '__main__':
    print problem40()
