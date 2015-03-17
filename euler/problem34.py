# -*- encoding: utf-8 -*-

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import itertools
import math


factorials = {
    '0': math.factorial(0),
    '1': math.factorial(1),
    '2': math.factorial(2),
    '3': math.factorial(3),
    '4': math.factorial(4),
    '5': math.factorial(5),
    '6': math.factorial(6),
    '7': math.factorial(7),
    '8': math.factorial(8),
    '9': math.factorial(9),
}


def find_approx_max():
    factorial_nine = factorials['9']
    for x in itertools.count(2):
        test = '9' * x
        if int(test) > (factorial_nine * x):
            return int('9' * x)
    return 0


def problem34():
    total = 0
    for x in range(10, find_approx_max()):
        current_sum = 0
        for d in str(x):
            current_sum += factorials[d]
        if current_sum == x:
            print x
            total += x
    return total


if __name__ == '__main__':
    print problem34()
