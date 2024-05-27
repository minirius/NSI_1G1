from math import *
# ------------ Fonction ------------ # 
def distance(A,xB,yB):
    """
    Fonction renvoyant la distance entre les points A et B
    Entrée 
    - xA, yA : type int --> Coordonnées du Point A 
    - xB, yB : type int --> Coordonnées du Point B

    Sortie : 
    - type float --> Distance entre le point A et le point B  
    """
    xA, yA=A
    
    return round(sqrt((xB-xA)**2+(yB-yA)**2))

def tri_distance_croissante(liste_origine,A):
    """
    Fonction qui renvoie une liste des points d'une liste donnée dans l'ordre croissant
    des distance séparant chacun de ces points d'un point donné
    Entrée : 
    - liste_origine : type list --> Liste de différent point dans le même repère orthonormé
    - A : type tuple --> Point à partir duquel on calcul la distance 

    Sortie : 
    - liste_organisée : type list --> liste des points de liste_origines organisée
    de façon croissante
    """
    assert type(liste_origine) == list and len(liste_origine) != 0

    for w in liste_origine:
        assert type(w) == tuple and len(w) == 2
    assert type(A) == tuple and len(A)==2

    for i in range(len(liste_origine)-1):
        for j in range(i+1,len(liste_origine)):
            if distance(liste_origine[j],A[0],A[1]) < distance(liste_origine[i],A[0],A[1]):
                liste_origine[i],liste_origine[j]=liste_origine[j],liste_origine[i]

    return(liste_origine)
        
        

# -------------- Main -------------- # 
if __name__ == '__main__':
    liste_origine=[(2,3),(3,1),(8,3),(7,4),(7,5),(2,6),(1,3),(5,8),(12,43),(7,2)]
    print(tri_distance_croissante(liste_origine, (0,0)))