def volBoite(l:int, p:int=None, h:int=None) -> int:
    """
    volBoite permet de calculer l'air d'une boite avec une geométrie différente en fonction des agruments
    Entrée : required l<int> : largeur de la boite
             optional p<int> : profondeur de la boite
             optional h<int> : hauteur de la boite
    Sortie : <int> : Volume de la Boite
    """
    if(p is None and h is None):
        return l**3
    elif(h is None):
        return l*l*p
    return l*p*h

print(volBoite(4, 3, 5))