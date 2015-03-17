# -*- encoding: utf-8 -*-

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import euler


def rotate(x):
    x = str(x)
    for n in range(0, len(x)):
        yield x[n:] + x[:n]


def problem35():
    primes = euler.generate_primes_by_eratosthenes(1000000)
    prime_set = set(primes)
    found = 0
    for prime in primes:
        circular_prime = True
        for x in rotate(prime):
            if int(x) not in prime_set:
                circular_prime = False
                break
        if circular_prime:
            found += 1
    return found


if __name__ == '__main__':
    print problem35()
