import decimal
from itertools import count


TEST_UNTIL = 1000
PREC_TEST = 1000
LIMIT = 2000


def multiplicative_order(a, n):
    for i in count(2, 1):
        if (a ** i) % n == 1:
            return i
        if i > LIMIT:
            return 1


def n_repeats(n):
    return len(str(1/decimal.Decimal(n))) >= (PREC_TEST + 2)


def problem26():
    decimal.getcontext().prec = PREC_TEST
    max_value = (0, 0)
    for i in xrange(2, TEST_UNTIL):
        if n_repeats(i):
            count = multiplicative_order(10, i)
        else:
            count = 1
        if count > max_value[1]:
            max_value = (i, count)
        print "%d %d" % (i, count)
    return max_value


if __name__ == '__main__':
    print problem26()
