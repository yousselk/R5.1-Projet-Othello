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

    def handle_click(self, mouse_pos, window_size=(480, 480)):
        """
        Gère un clic utilisateur sur la fenêtre de jeu.
        """
        cell_size = window_size[0] // self.board.size
        x, y = mouse_pos

        # Convertir les coordonnées en indices de grille
        col = x // cell_size
        row = y // cell_size

        # Tenter de placer un pion
        if self.board.place_piece(row, col, self.current_player):
            # Changer de joueur si le coup est valide
            self.current_player *= -1
