from safeType import *

nbr_allumettes = 21

def AI(a):
    b = 1
    print(a)
    if a == 1:
        b = 3
    elif a == 2:
        b = 2
    elif a == 3:
        b = 1
    return b

while True:
    for i in range(nbr_allumettes):
        print("|", end="")
    print(" ("+str(nbr_allumettes)+")")

    jeux_joueur = safeInt(input("Combien en prenez-vous ? "))
    while (1 > jeux_joueur or jeux_joueur > 3):
        jeux_joueur = safeInt(input("Combien en prenez-vous ? "))
    nbr_allumettes -= jeux_joueur

    if(nbr_allumettes <= 0):
        print("Vous avez perdu !")
        break

    jeux_ai = AI(jeux_joueur)
    nbr_allumettes -= jeux_ai
    print("J'en ai pris", jeux_ai)

    if(nbr_allumettes <= 0):
        print("Vous avez gagné !")
        break

