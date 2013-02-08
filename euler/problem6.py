

def euler_problem6(until):
    sum = 0
    sum_square = 0
    for i in range(1, until):
        sum += i
        sum_square += i * i
    return (sum * sum) - sum_square


def euler_problem6_2(until):
    sequence = map(lambda x: (x, x * x), range(1, until))
    sums = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), sequence)
    return (sums[0] * sums[0]) - sums[1]


def euler_problem6_3(until):
    seq = range(1, until)
    total = sum(seq)
    return total ** 2 - sum(x ** 2 for x in seq)


if __name__ == "__main__":
    print euler_problem6(101)
    print euler_problem6_2(101)
    print euler_problem6_3(101)
