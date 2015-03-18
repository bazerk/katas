# -*- encoding: utf-8 -*-

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import euler

TARGET = 11
primes = {2, 3, 5, 7}


def problem37():
    total = 0
    found = 0
    for p in euler.yield_primes(starting_from=11):
        primes.add(p)
        as_str = str(p)
        succeeds = True
        for x in xrange(1, len(as_str)):
            if int(as_str[x:]) not in primes or \
               int(as_str[0:len(as_str)-x]) not in primes:
                succeeds = False
                break
        if succeeds:
            total += p
            found += 1
        if found == TARGET:
            return total
    raise ValueError()


if __name__ == '__main__':
    print problem37()
