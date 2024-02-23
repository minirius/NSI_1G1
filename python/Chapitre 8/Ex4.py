def indexMax(liste:list) -> int:
    """
    IndexMax permet de trouver l'Index de la valeur la plus grande
    Entrée : liste<list<int>> : Liste de nombre dans lequel chercher la valeur max
    Sortie : <int> : Index de la valeur max de la liste
    """
    maxi = max(liste)
    for i, e in enumerate(liste):
        if(e == maxi): return i

print(indexMax([0, 4, 7, 23, 8, 2, 5]))