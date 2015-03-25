# -*- encoding: utf-8 -*-

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

import euler
import itertools
import math


MAX_VALUE = 1000000
DISTINCT = 4
primes = euler.generate_primes_by_eratosthenes(1000000)
primes_set = set(primes)

prime_factors = {}


def find_prime_factors(value):
    if value > MAX_VALUE:
        raise ValueError
    if value in primes_set:
        return [value]
    for p in primes:
        if value % p == 0:
            return [p] + find_prime_factors(value/p)
        if p > math.sqrt(value):
            break


def problem47():
    run = []
    for value in itertools.count(2):
        factors = set(find_prime_factors(value))
        if len(factors) == DISTINCT:
            run.append(value)
            if len(run) == DISTINCT:
                return run[0]
        else:
            run = []


if __name__ == '__main__':
    print problem47()
