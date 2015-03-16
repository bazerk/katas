# -*- encoding: utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools


PANDIGITAL = '123456789'
PAIRINGS = ((4, 1), (3, 2), )
found = set()


def check_new_pandigital(x, y, z):
    if z in found:
        return False
    joined = str(x) + str(y) + str(z)
    if len(joined) != 9:
        return False
    return ''.join(sorted(joined)) == PANDIGITAL


def check_pairing(a, b):
    total = 0
    for tst in itertools.permutations(PANDIGITAL, r=a + b):
        x = int(''.join(tst[:a]))
        y = int(''.join(tst[a:]))
        z = x * y
        if check_new_pandigital(x, y, z):
            total += z
            found.add(z)
            print '%d %d %d' % (x, y, z)
    return total


def problem32():
    count = 0
    for pairing in PAIRINGS:
        count += check_pairing(pairing[0], pairing[1])
    return count


if __name__ == '__main__':
    print problem32()
