from random import randint

def tableau_croissant(n):
	"""
	Génère un tableau aléatoire dont les éléments 
	sont des entiers naturels rangés dans l'odre croissant
	Entrée : un entier naturel n
	Sortie : un tableau de taille n, rangé dans l'ordre croissant
	"""
	tab = [randint(0, 10)]*n
	for i in range(1, n):
		tab[i] = tab[i - 1] + randint(0, 10)
	return tab


if __name__ == '__main__':
	def est_croissant(tab):
		"""
		Teste si les élts de tab sont rangés dans l'ordre croissant
		Entrée : tab une liste de nombres
		Sortie : un booléen
		"""
		for i in range(len(tab) - 1):
			if tab[i] > tab[i + 1]:
				return False
		return True
	
	for n in range(20):
		for _ in range(10):
			tab = tableau_croissant(n)
			assert est_croissant(tab)

