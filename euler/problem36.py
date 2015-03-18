# -*- encoding: utf-8 -*-

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def test_palindrome(tst):
    tst = str(tst)
    for i in xrange(0, len(tst)/2):
        if tst[i] != tst[-(i+1)]:
            return False
    return True


def problem36():
    total = 0
    for i in xrange(1, 1000000):
        if test_palindrome(i):
            binary = "{0:b}".format(i)
            if test_palindrome(binary):
                total += i
    return total


if __name__ == '__main__':
    print problem36()
