import random
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats 

#Print d'introduction
print("Graphique de Detection de Pi ")

def tire(nbrIteration):
    #Conteur de point dans et hors du cercle
    nbrPointInCercle = 0
    nbrPointOutCercle = 0
    #boucle
    for i in range(nbrIteration):
        #génération des point aleatoire (x, y)
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        #distance du point du coin bas gauche du carré,
        #permet de dire si le point est dans ou hors du cercle
        dist = math.sqrt((x-0)*(x-0)+(y-0)*(y-0))

        #test du cercle pour l'ajout dans le bon conteur
        if(dist > 1):
            nbrPointOutCercle += 1
        else:
            nbrPointInCercle +=1
    """
    #Sorties
    print(nbrPointOutCercle, nbrPointInCercle, nbrIteration)
    #calcul de pi par produit en crois (pi = (4*nbr de point dans le cercle)/nbr d'itération)
    print("pi = ", (4*nbrPointInCercle)/nbrIteration)

    difference = (abs(math.pi - (4*nbrPointInCercle)/nbrIteration)/math.pi)*100
    print("Erreur :", difference,"%")"""

    return (4*nbrPointInCercle)/nbrIteration

listIteration = []
listValeur = []

for i in range(1, 1000):
    valeur = tire(i)
    if(valeur < 3.2):
        listIteration.append(i)
        listValeur.append(valeur)


LI = np.array(listIteration)
LV = np.array(listValeur)

res = stats.linregress(LI, LV)

plt.plot(listIteration, listValeur)
plt.plot(LI, res.intercept + res.slope*LI, 'r', label='fitted line')
plt.show()