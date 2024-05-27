def premier(n):
	from math import sqrt
	
	"""
	Entrée : n un entier naturel 
	Sortie : Booléen
	
	Renvoie True si l'entier naturel n est premier et False sinon
	"""
	n = abs(n)
	if n == 0 or n == 1:
		return False
	# On teste les divisuerus potentiels jusqu'à racine de n.
	N = int(sqrt(n)) + 1
	for i in range(2, N):
		if n %i ==0 :
			return False
	return True


