import time
import matplotlib.pyplot as plt
import scipy.stats as stats

nbrIteration = 100
X, Y = [], []

for n in range(0, nbrIteration, 10):
    #génération des point aleatoire (x, y)
    #distance du point du coin bas gauche du carré,
    #permet de dire si le point est dans ou hors du cercle

    color = "blue"
    #test du cercle pour l'ajout dans le bon conteur
    #Généation du point sur le graphique
    #titre des Axes
    début = time.time()
    for i in range(n):
        for j in range(n):
            print(i, j)
    fin = time.time()
    temps = round(1000*(fin - début), 0)
    plt.title("Temps sur boucle for à 10*i 2D: "+ str(nbrIteration))
    plt.xlabel("Itération sur i (10*i)")
    plt.ylabel("Temps en ms")
    #Placement du point
    plt.scatter(n, temps, c = color)
    X.append(n)
    Y.append(temps)
    #Temps de repos
    plt.pause(1)


sns.regplot(x=X, y=Y, ci=None)
plt.show()