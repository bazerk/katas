import euler


def can_sum(number, a_set):
    for x in a_set:
        match = number - x
        if match in a_set:
            return True
    return False


def problem_euler23(until):
    (d, p, a) = euler.classify_numbers(range(1, until))
    a_set = set(a)
    total = 0
    for test in range(1, until):
        if not can_sum(test, a_set):
            total += test
    return total


if __name__ == '__main__':
    print problem_euler23(28124)
