import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
WINDOW_SIZE = (480, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Othello")

# Charger l'image du plateau
plateau_image = pygame.image.load("assets/plateau_othello.png")

# Redimensionner l’image au besoin (si elle n’est pas exactement 480x480)
plateau_image = pygame.transform.scale(plateau_image, WINDOW_SIZE)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Afficher l’image dans la fenêtre
    screen.blit(plateau_image, (0, 0))

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()
