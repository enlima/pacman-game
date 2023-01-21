import unittest

from pacman.game import find_pacman, move_pacman, play, is_valid_key, is_within_borders, is_a_wall, is_a_ghost, \
    is_there_remaining_pills


class GameTest(unittest.TestCase):

    def test_find_pacman(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 5)

    def test_find_pacman_when_pacman_doesnt_exist(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, -1)
        self.assertEqual(position_y, -1)

    def test_move_pacman(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

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

    def test_play_move_left(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(game_map, 'a')

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 4)

    def test_play_move_right(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(game_map, 'd')

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 3)
        self.assertEqual(position_y, 6)

    def test_play_move_up(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|..PP....|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(game_map, 'w')

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 2)
        self.assertEqual(position_y, 5)

    def test_play_move_down(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|..PP....|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        play(game_map, 's')

        position_x, position_y = find_pacman(game_map)

        self.assertEqual(position_x, 4)
        self.assertEqual(position_y, 5)

    def test_within_borders(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|......@.|",
            "|--------|"
        ]

        self.assertTrue(is_within_borders(game_map, 5, 8))
        self.assertTrue(is_within_borders(game_map, 4, 6))
        self.assertFalse(is_within_borders(game_map, 6, 10))
        self.assertFalse(is_within_borders(game_map, -1, 5))

    def test_is_a_wall(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|......@.|",
            "|--------|"
        ]

        self.assertTrue(is_a_wall(game_map, 4, 9))
        self.assertTrue(is_a_wall(game_map, 5, 7))
        self.assertFalse(is_a_wall(game_map, 4, 8))

    def test_is_a_ghost(self):
        game_map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G@....|.|",
            "|........|",
            "|--------|"
        ]

        self.assertTrue(is_a_ghost(game_map, 3, 1))
        self.assertFalse(is_a_ghost(game_map, 3, 3))

    def test_remaining_pills(self):
        game_map_with_pills = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        game_map_without_pills = [
            "|--------|",
            "|G..|..G.|",
            "|...@....|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        self.assertTrue(is_there_remaining_pills(game_map_with_pills))
        self.assertFalse(is_there_remaining_pills(game_map_without_pills))
