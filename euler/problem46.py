# -*- encoding: utf-8 -*-

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import itertools
import decimal
import euler
import math

MAX_VALUE = 100000


def problem46():
    primes = sorted(euler.generate_primes_by_eratosthenes(MAX_VALUE))
    prime_set = set(primes)
    for tst in itertools.count(9, 2):
        if tst > MAX_VALUE:
            ValueError
        if tst in prime_set:
            continue
        found_goldback = False
        for p in primes:
            if p > tst:
                break
            remainder = tst - p
            if remainder % 2 == 0:
                sqrt = math.sqrt(decimal.Decimal(remainder/2))
                if sqrt - int(sqrt) == 0:
                    found_goldback = True
                    break
        if not found_goldback:
            return tst


if __name__ == '__main__':
    print problem46()
