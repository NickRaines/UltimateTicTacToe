import unittest
from uttt_main import UTTT

class TestUTTT(unittest.TestCase):
    def test_get_valid_moves(self):
        game = UTTT()
        self.assertEqual(len(game.valid_moves), 81)
        game.make_move(4,1)
        print()
        game.print_board()

        self.assertEqual(len(game.valid_moves), 9)
        game.make_move(1,2)
        print()
        game.print_board()

        self.assertEqual(len(game.valid_moves), 9)
        game.make_move(2,4)
        print()
        game.print_board()

    def test_make_move(self):
        game = UTTT()
        self.assertTrue(game.make_move(0, 0))
        self.assertFalse(game.make_move(1,1))

    def test_generate_next_uttt(self):
        game = UTTT()
        valid_moves = game.get_valid_moves()
        next_game = game.generate_next_uttt(0, 0)
        # no idea how to test this ngl...

    def test_check_board_win(self):
        game = UTTT()
        game.game_grid[0][0] = 1
        game.game_grid[0][1] = 1
        game.game_grid[0][2] = 1
        self.assertTrue(game.check_board_win(0, 1))
        self.assertFalse(game.check_board_win(0, 2))

if __name__ == '__main__':
    unittest.main()