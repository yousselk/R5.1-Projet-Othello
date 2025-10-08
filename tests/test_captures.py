import unittest
from src.board import Board

# Test la capture de pions dans différentes directions
class TestCaptures(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.board = [[0 for _ in range(8)] for _ in range(8)]  # Plateau vide

    def test_horizontal_capture(self):
        # Prépare un alignement : Noir - Blanc - ? -> placement ici doit capturer en horizontal
        self.board.board[3][2] = -1  # Noir
        self.board.board[3][3] = 1   # Blanc

        result = self.board.place_piece(3, 4, -1)  # Noir joue à droite

        self.assertTrue(result)
        self.assertEqual(self.board.board[3][3], -1)  # Le pion blanc doit être capturé
        self.assertEqual(self.board.board[3][4], -1)  # Le nouveau pion est bien placé

    def test_vertical_capture(self):
        # Prépare un alignement vertical : Noir - Blanc - ?
        self.board.board[2][3] = -1  # Noir
        self.board.board[3][3] = 1   # Blanc

        result = self.board.place_piece(4, 3, -1)  # Noir joue en dessous

        self.assertTrue(result)
        self.assertEqual(self.board.board[3][3], -1)  # Le pion blanc est capturé
        self.assertEqual(self.board.board[4][3], -1)

    def test_diagonal_capture(self):
        # Prépare un alignement diagonal (↘)
        self.board.board[2][2] = -1  # Noir
        self.board.board[3][3] = 1   # Blanc

        result = self.board.place_piece(4, 4, -1)  # Noir joue en diagonale

        self.assertTrue(result)
        self.assertEqual(self.board.board[3][3], -1)  # Capture diagonale
        self.assertEqual(self.board.board[4][4], -1)

if __name__ == '__main__':
    unittest.main()
