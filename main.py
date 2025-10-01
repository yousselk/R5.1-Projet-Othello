from src.board import Board
from src.display import Display
import pygame
import sys

def main():
    board = Board()  # Initialise le plateau
    display = Display(board)  # Initialise la fenêtre de jeu

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.draw_board() # Affiche le plateau

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
