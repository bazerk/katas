import math
import collections
import itertools


def total_primes(count):
    primes = []
    test = 2
    while len(primes) < count:
        if test_prime(test):
            primes.append(test)
        test += 1
    return primes


def test_prime(number):
    for test in range(2, int(math.sqrt(number)) + 1):
        if number % test == 0:
            return False
    return True


def yield_primes(starting_from=2):
    for i in itertools.count(starting_from):
        if test_prime(i):
            yield i


def generate_triangle_numbers():
    '''Will generate triangle numbers indefinitely'''
    total = 0
    i = 1
    while 1:
        total += i
        i += 1
        yield total


def iterator_divisors(number, include_self=False):
    yield 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            yield i
            pair = number / i
            if pair != i:
                yield pair
    if include_self:
        yield number


def count_divisors(number):
    '''Cheats a bit and so wont work when number=1'''
    count = 2
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            count += 2
    return count


def classify_numbers(numbers):
    deficient = []
    perfect = []
    abundant = []
    for n in numbers:
        divisor_sum = sum(iterator_divisors(n))
        if divisor_sum < n:
            deficient.append(n)
        elif divisor_sum == n:
            perfect.append(n)
        else:
            abundant.append(n)

    return (deficient, perfect, abundant)


def generate_primes_by_eratosthenes(until):
    if until == 1:
        return []
    candidates = [2] + range(3, until, 2)
    ixTest = 0
    ixNext = 0
    limit = int(math.sqrt(until)) + 1
    while ixNext != -1:
        ixNext = -1
        for idx in range(ixTest + 1, len(candidates)):
            if candidates[idx] == -1:
                continue
            if candidates[idx] % candidates[ixTest] == 0:
                candidates[idx] = -1
            elif ixNext == -1:
                ixNext = idx
        ixTest = ixNext
        if candidates[ixTest] >= limit:
            break

    return filter(lambda c: c != -1, candidates)


def generate_pascals_triangles(max_level):
    numbers = [1]
    while len(numbers) <= max_level:
        yield numbers
        numbers = [1] + fold_list_for_pascal(numbers) + [1]
    yield numbers


def generate_fibbonaci():
    prev = 1
    current = 1
    while 1:
        yield current
        current = current + prev
        prev = current - prev


def fold_list_for_pascal(numbers):
    ret_list = []
    for i in range(len(numbers) - 1):
        ret_list.append(numbers[i] + numbers[i + 1])
    return ret_list


def traverse_triangle_max_sum(triangle):
    max_to_index = []
    for level in triangle:
        if len(level) == 1:
            max_to_index = [level[0]]
            continue
        max_to_this_level = []
        for idx, val in enumerate(level):
            max_parents = []
            if idx > 0:
                max_parents.append(max_to_index[idx - 1])
            if idx < (len(max_to_index)):
                max_parents.append(max_to_index[idx])
            max_to_this_level.append(max(max_parents) + val)
        max_to_index = max_to_this_level
    return max(max_to_index)

Point = collections.namedtuple('Point', ['x', 'y'])


class Vector(Point):
    def __add__(self, point):
        return Vector(self[0] + point[0], self[1] + point[1])


EulerDate = collections.namedtuple('EulerDate',
                                   ['day', 'month', 'year', 'weekday'])


def days_in_month(date):
    if date.month == 2:
        return 29 if is_leap_year(date.year) else 28
    days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[date.month]


def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0:
        return year % 400 == 0
    return True
