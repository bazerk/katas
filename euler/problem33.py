# -*- encoding: utf-8 -*-

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import euler


def generate_numerators(digit, denominator):
    digit = str(digit)
    for x in xrange(0, 10):
        value = int(digit + str(x))
        if value >= denominator:
            break
        yield (value, x)
    for x in range(1, 10):
        value = int(str(x) + digit)
        if value >= denominator:
            break
        yield (value, x)


def find_curious_fractions():
    fractions = []
    for denominator in xrange(11, 99):
        a = int(str(denominator)[0])
        b = int(str(denominator)[1])
        if b != 0:
            for value in generate_numerators(a, denominator - 1):
                if float(value[1])/b == float(value[0])/denominator:
                    fractions.append((value[0], denominator))
        if a == b or b == 0:
            continue
        for value in generate_numerators(b, denominator - 1):
            if float(value[1])/a == float(value[0])/denominator:
                fractions.append((value[0], denominator))
    return fractions


def problem33():
    fractions = find_curious_fractions()
    if len(fractions) != 4:
        raise ValueError('Expected four fractions')
    numerator = 1
    denominator = 1
    for f in fractions:
        numerator *= f[0]
        denominator *= f[1]
    print 'product of fractions is {0}/{1}'.format(numerator, denominator)
    divisors_numerator = set((x for x in euler.iterator_divisors(numerator, include_self=True)))
    divisors_denominator = sorted((x for x in euler.iterator_divisors(denominator, include_self=True)))
    divisor = 0
    for x in reversed(divisors_denominator):
        if x in divisors_numerator:
            divisor = x
            break
    if divisor > 0:
        return denominator/divisor
    return denominator


if __name__ == '__main__':
    print problem33()
