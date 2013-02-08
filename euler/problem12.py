import euler


def euler_problem12():
    for number in euler.generate_triangle_numbers():
        if euler.count_divisors(number) > 500:
            return number

if __name__ == '__main__':
    print euler_problem12()
