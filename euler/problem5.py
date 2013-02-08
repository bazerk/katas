

def euler_problem5(factors):
    max_factor = max(factors)
    test = max_factor
    while not is_evenly_divisible(test, factors):
        test += max_factor
    return test


def is_evenly_divisible(test, factors):
    return all(test % factor == 0 for factor in factors)
