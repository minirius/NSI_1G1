import random

tableau_ligne = [random.randint(0,100) for i in range(64)]
print(tableau_ligne)
tableau = [[0 for i in range(8)] for j in range(8)]
for i, e in enumerate(tableau_ligne):
    tableau[i//8][i%8] = e

print(tableau)