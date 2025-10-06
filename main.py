from src.display import Display
from src.game import Game
import pygame
import sys

def main():
    pygame.init()

    game = Game()               # Contient le plateau + la logique de tour
    display = Display(game)     # Affiche le plateau + pions

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Récupérer la position du clic
                mouse_pos = pygame.mouse.get_pos()
                # Appeler la logique de jeu
                game.handle_click(mouse_pos)

        # Afficher le plateau et les pions à jour
        display.draw_board()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
