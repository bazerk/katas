#!/usr/bin/python
import euler
import collections


def euler_problem15_fast(grid_length):
    return [seq for seq in euler.generate_pascals_triangles(2 * grid_length)][-1][grid_length]


def euler_problem15(grid_length):
    '''
    This solution is too slow
    '''
    routes = 0
    end_pos = (grid_length, grid_length)

    positions = collections.deque()
    positions.append((0, 0))

    while len(positions) > 0:
        position = positions.pop()
        if position == end_pos:
            routes += 1
        else:
            if position[0] <= grid_length:
                positions.append((position[0] + 1, position[1]))
            if position[1] <= grid_length:
                positions.append((position[0], position[1] + 1))
    return routes

if __name__ == "__main__":
    print euler_problem15_fast(20)
