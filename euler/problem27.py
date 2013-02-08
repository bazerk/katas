import euler


def run_sequence(a, b):
    n = 0
    while True:
        test = n ** 2 + a * n + b
        if test <= 0 or not euler.test_prime(test):
            break
        n += 1
    return n


def euler_problem27():
    candidates = None
    max_length = -1
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            result = run_sequence(a, b)
            if result > max_length:
                max_length = result
                candidates = (a, b)
                print candidates
    return candidates[0] * candidates[1]

if __name__ == '__main__':
    print euler_problem27()
