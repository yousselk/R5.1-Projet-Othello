# Gère l'affichage graphique du jeu en utilisant Pygame
import pygame

class Display:    
    def __init__(self, game, window_size=(480, 480)):
        """
        Initialise la fenêtre de jeu et charge l'image du plateau.
        """
        pygame.init()
        self.game = game
        self.board = game.board
        self.window_size = window_size
        self.cell_size = window_size[0] // game.board.size
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Othello")
        self.plateau_image = pygame.image.load("assets/plateau_othello.png")
        self.plateau_image = pygame.transform.scale(self.plateau_image, window_size)

    def draw_board(self):
        """
        Affiche l'image du plateau dans la fenêtre.
        """
        # Affiche le plateau graphique en fond
        self.screen.blit(self.plateau_image, (0, 0))

        # Met à jour le titre de la fenêtre avec le joueur actif
        player_name = "Noir" if self.game.current_player == -1 else "Blanc"
        pygame.display.set_caption(f"Othello - Tour du joueur : {player_name}")

        # Dessine les pions présents sur le plateau
        self.draw_pieces()

        # Affiche les coups valides si la partie n’est pas finie
        if not self.game.game_over:
            valid_moves = self.board.get_valid_moves(self.game.current_player)
            self.draw_highlight(valid_moves)
        else:
            # Affiche le message de fin de partie
            self.draw_end_message(self.game.end_message)

        # Rafraîchit la fenêtre pour afficher les changements
        pygame.display.flip()
    
    def draw_pieces(self):
        """
        Dessine les pions noirs et blancs sur le plateau.
        """
        for row in range(self.board.size):
            for col in range(self.board.size):
                value = self.board.board[row][col] # Valeur dans la case (0, 1 ou -1)
                if value != 0:
                    color = (255, 255, 255) if value == 1 else (0, 0, 0)  # Blanc ou noir
                    # Calculer le centre de la case
                    x = col * self.cell_size + self.cell_size // 2
                    y = row * self.cell_size + self.cell_size // 2
                    # Dessiner le pion (cercle)
                    pygame.draw.circle(self.screen, color, (x, y), self.cell_size // 2 - 5)
    
    def draw_highlight(self, valid_moves):
        """
        Met en évidence les cases où le joueur actuel peut jouer.
        """
        for row, col in valid_moves:
            x = col * self.cell_size
            y = row * self.cell_size
            rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, (255, 255, 0), rect, 2)

    def draw_end_message(self, message):
        font = pygame.font.SysFont(None, 48)
        text_surface = font.render(message, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(self.window_size[0] // 2, self.window_size[1] // 2))
        self.screen.blit(text_surface, text_rect)
