

def euler_problem14(limit):
    max_so_far = 0
    max_start = 0
    for i in range(1, limit):
        test = run_sequence(i)
        if test > max_so_far:
            max_so_far = test
            max_start = i
    return max_start


def run_sequence(number):
    initial_value = number
    run_length = 1
    while number != 1:
        if number in sequences:
            return sequences[initial_value]
        run_length += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    return run_length


def euler_problem14_memoized(limit):
    max_so_far = 0
    max_start = 0
    for i in range(1, limit):
        test = run_sequence_memoized(i)
        if test > max_so_far:
            max_so_far = test
            max_start = i
    return max_start


sequences = {}


def run_sequence_memoized(number):
    initial_value = number
    run_length = 0
    while number != 1:
        if number in sequences:
            sequences[initial_value] = run_length + sequences[number]
            return sequences[initial_value]
        run_length += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
    run_length += 1
    sequences[initial_value] = run_length
    return run_length


if __name__ == "__main__":
    print euler_problem14_memoized(1000000)
