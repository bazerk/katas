# -*- encoding: utf-8 -*-

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import string


def _words():
    with open('p042_words.txt') as f:
        text = f.read()
        for x in text.split(','):
            yield x.replace('"', '')


def _triangle_numbers(until_n=5000):
    numbers = set()
    for n in xrange(1, until_n):
        tn = 0.5 * n * (n + 1)
        numbers.add(tn)
    return numbers, tn


def problem42():
    count = 0
    values = {}
    for ix, alpha in enumerate(string.ascii_uppercase):
        values[alpha] = ix + 1
    triangle_numbers, max_t = _triangle_numbers()
    for word in _words():
        word_total = 0
        for ch in word:
            word_total += values[ch]
        if word_total in triangle_numbers:
            count += 1
            print word
        elif word_total > max_t:
            raise ValueError
    return count


if __name__ == '__main__':
    print problem42()
