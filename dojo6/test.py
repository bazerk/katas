import unittest
from mars import calculate_positions


class MarsTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_robots_dont_move(self):
        input = \
"""5 3
0 0 E

0 0 E
"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 0 E', '0 0 E'])

    def test_robots_move_east(self):
        input = \
"""5 3
0 0 E
F
0 0 E
FF"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['1 0 E', '2 0 E'])

    def test_robots_spin(self):
        input = \
"""5 3
0 0 E
RR
0 0 E
LL"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 0 W', '0 0 W'])

    def test_robots_spin_and_move(self):
        input = \
"""5 3
2 0 E
RRFF
2 0 E
LLFF"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 0 W', '0 0 W'])

    def test_robots_move_x_and_y(self):
        input = \
"""5 3
2 0 E
RRFFRFF"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 2 N'])

    def test_crash_robot(self):
        input = \
"""2 2
0 0 W
F
0 0 S
F
2 0 E
F
0 2 N
F"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 0 W', '0 0 S', '2 0 E', '0 2 N'])

    def test_crashed_robots_dont_move(self):
        input = \
"""2 2
0 0 W
FRRFF"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 0 W'])

    def test_scent_markers(self):
        input = \
"""2 2
0 0 W
FR
0 0 W
FR"""
        positions = calculate_positions(input)
        self.assertEqual(positions, ['0 0 W', '0 0 N'])

if __name__ == '__main__':
    unittest.main()
