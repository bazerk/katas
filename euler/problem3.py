import math


def euler_problem3(number):
    largest_factor = None
    for test in range(3, int(math.sqrt(number)), 2):
        if number % test == 0 and test_prime(test):
            largest_factor = test
    return largest_factor


def test_prime(number):
    for test in range(2, int(math.sqrt(number)) + 1):
        if number % test == 0:
            return False
    return True
