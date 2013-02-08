from collections import namedtuple

Position = namedtuple('Position', 'x y facing')
Vector = namedtuple('Vector', 'x y')


def calculate_positions(input):
    scent_markers = set()
    lines = input.split('\n')
    split_mesa = lines[0].split(' ')
    mesa = Vector(int(split_mesa[0]), int(split_mesa[1]))

    end_positions = []

    for ixLine in range(1, len(lines), 2):
        split_start_pos = lines[ixLine].split(' ')
        position = Position(int(split_start_pos[0]), int(split_start_pos[1]), split_start_pos[2])
        instructions = lines[ixLine + 1]
        position = move_robot(mesa, scent_markers, position, instructions)
        end_positions.append('{0} {1} {2}'.format(position.x, position.y, position.facing))

    return end_positions


def move_robot(mesa, scent_markers, position, instructions):
    for instruction in instructions:
        marker = '{0}-{1}'.format(position, instruction)
        if marker in scent_markers:
            continue
        new_position = apply_to_robot(position, instruction)
        if new_position.x < 0 or new_position.y < 0 or new_position.x >= mesa.x or new_position.y >= mesa.y:
            scent_markers.add(marker)
            return position  # craaaaaaaaaaaaaaaaaaaaaaaaaaaash
        position = new_position
    return position

forward = {
    'W': Vector(-1, 0),
    'N': Vector(0, 1),
    'E': Vector(1, 0),
    'S': Vector(0, -1),
}

rotate = {
    'L': {'W': 'S', 'S': 'E', 'E': 'N', 'N': 'W'},
    'R': {'W': 'N', 'N': 'E', 'E': 'S', 'S': 'W'},
}


def apply_to_robot(position, instruction):
    if instruction == 'F':
        move = forward[position.facing]
        return Position(position.x + move.x, position.y + move.y, position.facing)
    return Position(position.x, position.y, rotate[instruction][position.facing])
