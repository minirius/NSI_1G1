def tri_pairs(liste_origine):
    """
    retourne la liste contenant tous les nombres entiers pairs
    contenus dans une liste de nombres entiers naturels entrée 
    en paramètre
    
    Arguments : 
    entree : liste d'entiers naturels

    Sortie : 
    sortie : liste d'entiers naturels
    """
    
    return [nb for nb in liste_origine if nb%2==0]

