from safeType import *
import random

bateau = (random.randint(0, 9), random.randint(0, 4))

HEIGHT = 10
WIDTH = 10

game = True
nbrTir = 0
grille = []
for i in range(0, HEIGHT):
    ligne = []
    for j in range(0, WIDTH):
        ligne.append(0)
    grille.append(ligne)

def render():
    print(" ", end=" ")
    for i in range(0, WIDTH):
        print(i, end=" ")
    print()
    for i, ligne in enumerate(grille):
        print(i, end=' ')
        for case in ligne : 
            if case == 0: print(".", end=" ")
            elif case == 1: print("X", end=" ")
            else: print("O", end=" ")
            
        print()

def log(string):
    print("----------------")
    print(string)
    print("----------------")

render()
while game == True:
    x = safeInt(input("x: "))
    y = safeInt(input("y: "))
    if(not(0 <= x <= WIDTH-1) or not(0 <= y <= HEIGHT-1)):
        log("Nombre invalide !")
        render()
        continue
    ##print(x, y)
    if(x == bateau[0] and y == bateau[1]):
        nbrTir += 1
        log("Touché en "+str(nbrTir)+" coup(s) !")
        grille[y][x] = 2
        game = False
    else:
        nbrTir += 1
        if x == bateau[0] or y == bateau[1]:
            log("En Vue !")
        else:
            log("A l'eau !")
        grille[y][x] = 1
    render()