import euler


def euler_problem67():
    triangle = []
    with open('triangle.txt') as f:
        input = f.read()
    for line in input.splitlines():
        triangle.append([int(x) for x in line.split()])
    return euler.traverse_triangle_max_sum(triangle)


if __name__ == '__main__':
    print euler_problem67()
