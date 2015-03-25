# -*- encoding: utf-8 -*-

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from collections import defaultdict
import euler

SKIP = '148748178147'
INC_BY = 3330


def _test_set(prime_set):
    for ix in range(0, len(prime_set) - 2):
        p = prime_set[ix]
        if (p + INC_BY) in prime_set and (p + INC_BY * 2) in prime_set:
            value = str(p) + str(p + INC_BY) + str(p + INC_BY * 2)
            if value != SKIP:
                return value


def problem49():
    primes = filter(lambda p: p >= 1000, euler.generate_primes_by_eratosthenes(10000))
    prime_sets = defaultdict(list)
    for prime in primes:
        key = ''.join(sorted(str(prime)))
        prime_sets[key].append(prime)
    for k in prime_sets:
        prime_set = prime_sets[k]
        if len(prime_set) >= 3:
            found = _test_set(prime_set)
            if found is not None:
                return found
    raise ValueError


if __name__ == '__main__':
    print problem49()
