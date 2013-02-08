

def populate_spiral(grid, spiral, counter, middle):
    if spiral == 0:
        grid[middle][middle] = counter
        return counter + 1
    x = middle + spiral
    y = middle - (spiral - 1)
    spiral_side_length = spiral * 2 + 1
    # go down
    for y in range(y, y + (spiral_side_length - 1)):
        grid[y][x] = counter
        counter += 1
    # go left
    for x in range(x - 1, x - spiral_side_length, -1):
        grid[y][x] = counter
        counter += 1
    # go up
    for y in range(y - 1, y - spiral_side_length, -1):
        grid[y][x] = counter
        counter += 1
    # go right
    for x in range(x + 1, x + spiral_side_length, 1):
        grid[y][x] = counter
        counter += 1
    return counter


def generate_spiral(length):
    if length % 2 != 1:
        raise Exception("length of a spiral must be odd")

    grid = [[0] * length for x in range(length)]
    middle = (length / 2)
    counter = 1
    for spiral in range(0, (length / 2) + 1):
        counter = populate_spiral(grid, spiral, counter, middle)
    return grid


def euler_problem28():
    spiral_length = 1001
    spiral = generate_spiral(spiral_length)
    count = 0
    for ix in range(spiral_length):
        count += spiral[ix][ix]
        count += spiral[ix][spiral_length - ix - 1]
    return count - 1

if __name__ == '__main__':
    print euler_problem28()
