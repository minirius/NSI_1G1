import random
import math


tableau_ligne = [random.randint(0, 100) for i in range(64)]

SIZE = int(math.sqrt(len(tableau_ligne))) if math.sqrt(len(tableau_ligne)) == int(math.sqrt(len(tableau_ligne))) else int(math.sqrt(len(tableau_ligne))+1)
tableau = [[tableau_ligne[i+j*SIZE] if i+j*SIZE < len(tableau_ligne) else -1 for i in range(SIZE)] for j in range(SIZE)]


tableau = [[tableau_ligne[i+j*8] for i in range(8)] for j in range(8)]

tableau = [[0 for i in range(8)] for j in range(8)]
for i, e in enumerate(tableau_ligne):
    tableau[i//8][i%8] = e


for sub in tableau:
    for e in sub:
        print(str(e).rjust(4), end=" ")
    print()