import unittest
from src.board import Board

# Test les fonctionnalités de base du plateau : initialisation, placement de pions, coups valides
class TestBoard(unittest.TestCase):
    def setUp(self):
        # Code exécuté avant chaque test : on crée un nouveau plateau
        self.board = Board()

    def test_initialization(self):
        # Vérifie que les 4 pions initiaux sont bien placés
        self.assertEqual(self.board.board[3][3], 1)  # blanc
        self.assertEqual(self.board.board[4][4], 1)  # blanc
        self.assertEqual(self.board.board[3][4], -1) # noir
        self.assertEqual(self.board.board[4][3], -1) # noir

    def test_place_piece_valid(self):
        # Test placement légal (exemple pion noir à (2,3) sur plateau initial)
        result = self.board.place_piece(2, 3, -1)
        self.assertTrue(result)
        # Vérifie que le pion est bien placé
        self.assertEqual(self.board.board[2][3], -1)
        # Vérifie qu’au moins un pion adverse a été retourné
        self.assertEqual(self.board.board[3][3], -1)

    def test_place_piece_invalid(self):
        # Test placement illégal (exemple case vide sans capture)
        result = self.board.place_piece(0, 0, 1)
        self.assertFalse(result)
        # La case doit rester vide
        self.assertEqual(self.board.board[0][0], 0)

    def test_get_valid_moves(self):
        # Vérifie que les coups valides pour noir sont ceux attendus sur plateau initial
        valid_moves = self.board.get_valid_moves(-1)
        expected_moves = [(2, 3), (3, 2), (4, 5), (5, 4)] # liste des coups valides attendus
        for move in expected_moves:
            self.assertIn(move, valid_moves)
        self.assertEqual(len(valid_moves), len(expected_moves))

if __name__ == '__main__':
    unittest.main()
