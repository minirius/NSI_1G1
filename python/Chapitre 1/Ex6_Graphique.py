import random
import math
import matplotlib.pyplot as plt

#Print d'introduction
print("Graphique de Detection de Pi ")

itération = 5000

def tire(nbrIteration):
    #Conteur de point dans et hors du cercle
    nbrPointInCercle = 0
    nbrPointOutCercle = 0
    plt.ion()
    #boucle
    for i in range(nbrIteration):
        #génération des point aleatoire (x, y)
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        #distance du point du coin bas gauche du carré,
        #permet de dire si le point est dans ou hors du cercle
        dist = math.sqrt((x-0)*(x-0)+(y-0)*(y-0))

        color = "blue"
        #test du cercle pour l'ajout dans le bon conteur
        if(dist > 1):
            nbrPointOutCercle += 1
            color = "red"
        else:
            nbrPointInCercle +=1
        
        #Généation du point sur le graphique
        #titre des Axes
        plt.title("Nombre d'itération : "+ str(nbrIteration))
        plt.xlabel("X")
        plt.ylabel("Y")
        #Placement du point
        plt.scatter(x, y, c = color)
        #Temps de repos
        plt.pause(0.005)

    return (4*nbrPointInCercle)/nbrIteration

for i in range(1, itération):
    valeur = tire(i)
