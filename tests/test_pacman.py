import unittest

from pacman_game.pacman import find_pacman, move_pacman


class PacmanTest(unittest.TestCase):

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
