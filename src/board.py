# Contient la class Board qui gère la logique du plateau de jeu

# Classe Board : gère la logique du plateau de jeu Othello
class Board:
	def __init__(self, size=8):
		"""
		Initialise le plateau de jeu Othello.
		- size : taille du plateau (par défaut 8x8)
		- self.board : matrice 2D représentant le plateau
		Les cases vides sont à 0, les pions blancs à 1, les noirs à -1.
		Place les 4 pions initiaux au centre du plateau.
		"""
		self.size = size
		self.board = [[0 for _ in range(size)] for _ in range(size)]
		# Initialisation des 4 pions centraux selon les règles Othello
		self.board[3][3] = 1    # Blanc
		self.board[4][4] = 1    # Blanc
		self.board[3][4] = -1   # Noir
		self.board[4][3] = -1   # Noir

	def display_console(self):
		"""
		Affiche le plateau dans la console.
		Utilise des symboles pour chaque type de case :
		. = case vide, B = pion blanc, N = pion noir
		"""
		symbols = {0: '.', 1: 'B', -1: 'N'}
		for row in self.board:
			print(' '.join(symbols[cell] for cell in row))

    # Ne gère pas encore la capture des pions adverses
	def place_piece(self, row, col, color):
		"""
		Place un pion sur le plateau à la position (row, col).
		- color : 1 pour blanc, -1 pour noir
		Place le pion seulement si la case est vide.
		Retourne True si le placement est réussi, False sinon.
		"""
		if self.board[row][col] == 0:
			self.board[row][col] = color
			return True
		return False

# Test de la classe Board
if __name__ == "__main__":
	b = Board()
	print("Plateau initial :")
	b.display_console()
	print("\nPlacement d'un pion blanc en (2,3):")
	b.place_piece(2, 3, 1)
	b.display_console()
	print("\nPlacement d'un pion noir en (4,5):")
	b.place_piece(4, 5, -1)
	b.display_console()
    