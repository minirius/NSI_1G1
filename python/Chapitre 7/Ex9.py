import random
import math


tableau_ligne = [random.randint(0, 100) for i in range(365)]

SIZE = int(math.sqrt(len(tableau_ligne))) if math.sqrt(len(tableau_ligne)) == int(math.sqrt(len(tableau_ligne))) else int(math.sqrt(len(tableau_ligne))+1)
tableau = [[tableau_ligne[i+j*SIZE] if i+j*SIZE < len(tableau_ligne) else 0 for i in range(SIZE)] for j in range(SIZE)]

for sub in tableau:
    for e in sub:
        print(str(e).rjust(3), end=" ")
    print()