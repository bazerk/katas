import euler


def euler_problem7(find_nth_prime):
    return euler.total_primes(find_nth_prime)[-1]

if __name__ == "__main__":
    print euler_problem7(10001)
