import random
import time

def table(n:int) -> None:
    """
    Fonction qui écrit la table de n sur 20
    """
    for i in range(1, 21): print(f"{str(i).ljust(2)} x {n} = {i*n}")

def jeu():
    """
    Petit Jeu qui permet de tester les multiplications
    """
    nbrMax = int(input("Nombre maximum ? : "))
    startTime = time.time()
    nbrErreur = 0
    for i in range(10):
        a, b = random.randint(2, nbrMax), random.randint(2, nbrMax)
        reponse = int(input(f"{a} x {b} = "))
        if(reponse != a*b):
            print("Faux !")
            bonneReponse = False
            nbrErreur += 1
            while not bonneReponse:
                reponse = int(input(f"{a} x {b} = "))
                if(reponse == a*b): bonneReponse = True
                else : print("Toujours pas !");nbrErreur += 1
    stopTime = time.time()
    print("-------------------")
    print("Terminé ! ")
    print()
    print("Temps:", str(round(stopTime-startTime))+"s")
    print("Errerus:", nbrErreur)
    print("-------------------")

jeu()