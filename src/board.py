# Classe Board : gère la logique du plateau de jeu Othello
class Board:
	# Liste des directions (8 directions)
	DIRECTIONS = [
		(0, 1),     # droite
		(0, -1),    # gauche
		(1, 0),     # bas
        (-1, 0),    # haut
		(1, 1),     # bas-droite
		(1, -1),    # bas-gauche
		(-1, 1),    # haut-droite
		(-1, -1)    # haut-gauche
	]

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

	def place_piece(self, row, col, color):
		"""
		Place un pion sur le plateau à la position (row, col).
		- color : 1 pour blanc, -1 pour noir
		Place le pion seulement si la case est vide et effectue la capture des pions adverses.
		Retourne True si le placement est réussi, False sinon.
		"""
		if self.board[row][col] != 0:
			return False
        
		to_flip = []  # Liste des positions des pions à retourner
		for dr, dc in self.DIRECTIONS:
			# On récupère les positions des pions adverses à retourner dans cette direction
			flips = self._get_flips(row, col, dr, dc, color)
			if flips:
				# Si des pions sont à retourner, on les ajoute à la liste globale
				to_flip.extend(flips)
		# Si au moins un pion adverse est capturé, le coup est légal
		if to_flip:
			# On place le pion du joueur sur la case choisie
			self.board[row][col] = color
			# On retourne tous les pions adverses capturés
			for r, c in to_flip:
				self.board[r][c] *= -1  # Multiplie par -1 pour changer la couleur
			return True
		return False
	def has_valid_move(self, color):
		"""
		Vérifie si le joueur actif a au moins un coup valide.
		"""
		return bool(self.get_valid_moves(color))
	
	def get_valid_moves(self, color):
		"""
		Retourne une liste des coups valides pour le joueur actif.
		"""
		moves = []
		for row in range(self.size):
			for col in range(self.size):
				if self.board[row][col] == 0:
					for dr, dc in self.DIRECTIONS:
						if self._get_flips(row, col, dr, dc, color):
							moves.append((row, col))
							break
		return moves

	def _get_flips(self, row, col, dr, dc, color):
		"""
		Cherche les pions à retourner dans une direction donnée à partir de la case (row, col).
		- dr, dc : direction (delta row, delta col)
		- color : couleur du joueur qui joue (1 ou -1)
		Retourne la liste des positions à retourner si le coup est légal dans cette direction, sinon []
		"""
		flips = []  # Liste des positions des pions adverses rencontrés
		r, c = row + dr, col + dc  # On avance d'une case dans la direction
		# On parcourt le plateau dans la direction tant qu'on reste dans les limites
		while 0 <= r < self.size and 0 <= c < self.size:
			if self.board[r][c] == -color:
				# Si on trouve un pion adverse, on l'ajoute à la liste
				flips.append((r, c))
			elif self.board[r][c] == color:
				# Si on trouve un pion de la même couleur après des adverses, le coup est légal
				return flips if flips else []  # On retourne la liste si au moins un pion adverse a été rencontré
			else:
				# Si on tombe sur une case vide ou hors plateau, le coup n'est pas légal dans cette direction
				break
			r += dr  # Avancer dans la direction
			c += dc
		# Si on n'a pas trouvé de pion de la même couleur, on ne retourne rien
		return []

# Test de la classe Board
if __name__ == "__main__":
	b = Board()
	print("Plateau initial :")
	b.display_console()
	print("\nPlacement d'un pion blanc en (2,3): Coup non légal")
	b.place_piece(2, 3, 1)
	b.display_console()
	print("\nPlacement d'un pion noir en (4,5): Coup légal")
	b.place_piece(4, 5, -1)
	b.display_console()
    