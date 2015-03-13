import itertools


def find_max_digits():
    nine_pow_5 = 9 ** 5
    for digits in itertools.count(2, 1):
        if (nine_pow_5 * digits) < int('9' * digits):
            return digits


def problem30():
    max_digits = find_max_digits()
    sum_total = 0
    for n in xrange(11, int('9' * max_digits)):
        power_5_sum = 0
        for d in str(n):
            power_5_sum += int(d) ** 5
        if power_5_sum == n:
            sum_total += n
            print n
    return sum_total

if __name__ == '__main__':
    print problem30()
