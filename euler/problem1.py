

def euler_problem1(upper_threshold):
    return sum([x for x in range(1, upper_threshold) if (x % 3 == 0) or (x % 5 == 0)])
