import unittest

from pacman.game import find_pacman, move_pacman, is_within_borders, is_a_wall, is_a_ghost, \
    is_there_remaining_pills, calculate_next_position, recreate_line
from pacman.ui import is_valid_key


def get_map():
    return [
        "|--------|",
        "|G..|..G.|",
        "|...PP...|",
        "|G...@.|.|",
        "|........|",
        "|--------|"
    ]


def get_map_limits():
    return [
        "|--------|",
        "|G..|..G.|",
        "|...PP...|",
        "|G.....|.|",
        "|......@.|",
        "|--------|"
    ]


class GameTest(unittest.TestCase):

    def test_find_pacman(self):
        game_map = get_map()

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 5)

    def test_find_pacman_when_pacman_doesnt_exist(self):
        game_map_no_pacman = ["|--------|", "|--------|"]

        position_x, position_y = find_pacman(game_map_no_pacman)

        self.assertEqual(position_x, -1)
        self.assertEqual(position_y, -1)

    def test_move_pacman(self):
        game_map = get_map()

        move_pacman(game_map, 4, 1)

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 4)
        self.assertEqual(position_y, 1)

    def test_is_valid_key(self):
        self.assertTrue(is_valid_key('a'))
        self.assertTrue(is_valid_key('A'))
        self.assertTrue(is_valid_key('w'))
        self.assertTrue(is_valid_key('W'))
        self.assertTrue(is_valid_key('d'))
        self.assertTrue(is_valid_key('D'))
        self.assertTrue(is_valid_key('s'))
        self.assertTrue(is_valid_key('S'))
        self.assertFalse(is_valid_key('x'))
        self.assertFalse(is_valid_key('y'))

    def test_calculate_next_position(self):
        game_map = get_map()

        self.assertEqual((calculate_next_position(game_map, 'a')), (3, 4))
        self.assertEqual((calculate_next_position(game_map, 'd')), (3, 6))
        self.assertEqual((calculate_next_position(game_map, 'w')), (2, 5))
        self.assertEqual((calculate_next_position(game_map, 's')), (4, 5))

    def test_is_within_borders(self):
        game_map = get_map_limits()

        self.assertTrue(is_within_borders(game_map, 5, 8))
        self.assertTrue(is_within_borders(game_map, 4, 6))
        self.assertFalse(is_within_borders(game_map, 6, 10))
        self.assertFalse(is_within_borders(game_map, -1, 5))

    def test_is_a_wall(self):
        game_map = get_map_limits()
        self.assertTrue(is_a_wall(game_map, 4, 9))
        self.assertTrue(is_a_wall(game_map, 5, 7))
        self.assertFalse(is_a_wall(game_map, 4, 8))

    def test_is_a_ghost(self):
        game_map = get_map()

        self.assertTrue(is_a_ghost(game_map, 3, 1))
        self.assertFalse(is_a_ghost(game_map, 3, 5))

    def test_is_there_remaining_pills(self):
        game_map = get_map()
        game_map_no_pills = [
            "|--------|",
            "|G..|..G.|",
            "|...@....|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        self.assertTrue(is_there_remaining_pills(game_map))
        self.assertFalse(is_there_remaining_pills(game_map_no_pills))

    def test_recreate_line(self):
        game_map = get_map()

        self.assertEqual(recreate_line(game_map, 3, 5, '.'), "|G.....|.|")
        self.assertEqual(recreate_line(game_map, 4, 5, '@'), "|....@...|")
        self.assertEqual(recreate_line(game_map, 2, 1, 'G'), "|G..PP...|")
