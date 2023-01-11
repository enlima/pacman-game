import unittest

from pacman.game import find_pacman, move_pacman, play, is_valid_key


class GameTest(unittest.TestCase):

    def test_find_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 5)

    def test_find_pacman_when_pacman_doesnt_exist(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, -1)
        self.assertEqual(position_y, -1)

    def test_move_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        move_pacman(map, 4, 1)

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, 4)
        self.assertEqual(position_y, 1)

    def test_valid_key(self):
        self.assertTrue(is_valid_key('a'))
        self.assertTrue(is_valid_key('A'))
        self.assertTrue(is_valid_key('w'))
        self.assertTrue(is_valid_key('W'))
        self.assertTrue(is_valid_key('d'))
        self.assertTrue(is_valid_key('D'))
        self.assertTrue(is_valid_key('s'))
        self.assertTrue(is_valid_key('S'))

    def test_invalid_key(self):
        self.assertFalse(is_valid_key('x'))
        self.assertFalse(is_valid_key('y'))

    def test_play_move_left(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(map, 'a')

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 4)

    def test_play_move_right(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(map, 'd')

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 6)

    def test_play_move_up(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|..PP....|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(map, 'w')

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, 2)
        self.assertEqual(position_y, 5)

    def test_play_move_down(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|..PP....|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(map, 's')

        position_x, position_y = find_pacman(map)

        self.assertEqual(position_x, 4)
        self.assertEqual(position_y, 5)
