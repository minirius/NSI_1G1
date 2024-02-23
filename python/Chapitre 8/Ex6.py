def eleMax(liste:list, début:int=0, fin:int=None) -> int:
    """
    eleMax permet de trouver le Maximum d'une liste sur un plage donnée
    Entrée : required liste<list<int>> : Liste avec les outils à chercher
             optional début<int> : Début de plage
             optional fin<int> : Fin de plage
    Sortie : <int> : Maximum trouvé sur la plage donnée
    """
    if(fin is None): fin = len(liste)
    maxi = max(liste[début:fin])
    return maxi

listes = [0, 5, 6, 4, 8, 2, 9, 7, 0, 4, 9]
print(eleMax(listes))