# -*- encoding: utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import euler
import itertools


def problem41():
    for num_digits in xrange(9, 0, -1):
        digits = [str(x) for x in range(num_digits, 0, -1)]
        for x in itertools.permutations(digits, r=num_digits):
            tst = int(''.join(x))
            if euler.faster_prime_test(tst):
                return tst
    raise ValueError()


if __name__ == '__main__':
    print problem41()
