import pygame
from src.board import Board

class Game:
    def __init__(self):
        """
        Initialise le jeu :
        - Crée le plateau (Board)
        - Définit le joueur actuel (noir)
        """
        self.board = Board()
        self.current_player = -1  # Noir commence toujours
        self.game_over = False   # Partie en cours
        self.end_message = ""

    def handle_click(self, mouse_pos, window_size=(480, 480)):
        """
        Gère un clic utilisateur sur la fenêtre de jeu.
        """
        if self.game_over:
            return  # Ignore les clics si le jeu est terminé
        
        cell_size = window_size[0] // self.board.size
        x, y = mouse_pos

        # Convertir les coordonnées en indices de grille
        col = x // cell_size
        row = y // cell_size

        # Tenter de placer un pion
        if self.board.place_piece(row, col, self.current_player):
            # Changer de joueur si le coup est valide
            self.current_player *= -1
        
        # Après un coup valide, vérifier si le joueur suivant peut jouer
        if not self.board.has_valid_move(self.current_player):
            # Aucun coup possible -> vérifier si l'autre joueur peut jouer
            if not self.board.has_valid_move(-self.current_player):
                print("Fin de partie.")
                self.end_game()
            else:
                print("Pas de coup possible pour ce joueur, on passe.")
                self.current_player *= -1

    def end_game(self):
        """
        Affiche le résultat de la partie.
        """
        self.game_over = True
        blacks = sum(row.count(-1) for row in self.board.board)
        whites = sum(row.count(1) for row in self.board.board)

        if blacks > whites:
            result = "Victoire des Noirs !"
        elif whites > blacks:
            result = "Victoire des Blancs !"
        else:
            result = "Égalité !"

        self.end_message = result
        pygame.display.set_caption(f"Othello - {result}")
