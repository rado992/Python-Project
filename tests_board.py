import unittest
from board import Board


CLASSIC_GAME = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5,
                0, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 0, 0]


TAKEOUT_GAME = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 5, 4, 2, 1, 0, 3, 0]


class BoardTest(unittest.TestCase):
    def test_new_board(self):
        board = Board()
        field = {}
        field['W'] = CLASSIC_GAME
        field['B'] = CLASSIC_GAME
        self.assertEqual(field, board.get_board())

    def test_move_tile(self):
        board = Board()
        board.move_checker('W', 1, 3)
        self.assertEqual(1, board.get_board()['W'][4])
        self.assertEqual(1, board.get_board()['W'][1])
        board.move_checker('W', 1, 3)
        self.assertEqual(2, board.get_board()['W'][4])
        self.assertEqual(0, board.get_board()['W'][1])

    def test_forbidden_move(self):
        board = Board()
        self.assertEqual(False, board.move_checker('W', 1, 5))

    def test_knock_tile(self):
        board = Board()
        board.move_checker('W', 1, 6)
        board.move_checker('B', 17, 1)
        #print(board.get_board())
        self.assertEqual(1, board.get_board()['W'][0])
        self.assertEqual(1, board.get_board()['B'][18])

    def test_takeout(self):
        board = Board(TAKEOUT_GAME)
        #print(board.get_board())
        board.move_checker('W', 19, 6)
        board.move_checker('W', 24, 1)
        self.assertEqual(False, board.move_checker('W', 24, 5))
        self.assertEqual(2, board.get_board()['W'][25])
        self.assertEqual(2, board.get_board()['W'][24])
        self.assertEqual(4, board.get_board()['W'][19])


    def test_dice_throw(self):
        board = Board()
        for i in range(50):
            for j in board.throw_dice():
                self.assertIn(j, range(7))




if __name__ == '__main__':
    unittest.main()