import unittest
from src.game import Game

# Test la logique de jeu : changement de tour après un coup valide
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_turn_switch_after_valid_move(self):
        # Vérifie que le joueur initial est bien le joueur noir (-1)
        self.assertEqual(self.game.current_player, -1)

        # Simule un clic sur la case (2,3), qui est un coup valide pour noir au départ
        # Taille de fenêtre par défaut : 480x480, donc chaque case fait 60px
        # Position x = col * 60 + 5 ; y = row * 60 + 5 pour viser le centre de la case (2,3)
        click_position = (3 * 60 + 5, 2 * 60 + 5)  # (col=3, row=2)

        self.game.handle_click(click_position, window_size=(480, 480))

        # Vérifie que le joueur courant a changé (devient blanc = 1)
        self.assertEqual(self.game.current_player, 1)

    def test_game_end_when_no_moves_for_both_players(self):
        game = Game()

        # On remplit tout le plateau avec des pions noirs, donc plus de coups possibles
        game.board.board = [[-1 for _ in range(8)] for _ in range(8)]

        # Supprime une seule case vide mais sans capture possible
        game.board.board[0][0] = 0

        # Blanc joue, mais aucun coup possible
        game.current_player = 1

        # Simule un clic sur la case vide, ce ne sera pas un coup valide
        game.handle_click((0 * 60 + 5, 0 * 60 + 5))

        # On attend que le jeu détecte la fin de partie
        self.assertTrue(game.game_over)
        self.assertIn("Victoire", game.end_message)  # Noir doit gagner
