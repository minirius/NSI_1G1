import random

HEIGHT = random.randint(1, 15)
WIDTH = random.randint(1, 15)

tableau_ligne = [random.randint(0, 100) for i in range(HEIGHT*WIDTH)]
print(tableau_ligne)

tableau = [[tableau_ligne[i+j*WIDTH] for i in range(WIDTH)] for j in range(HEIGHT)]


for sub in tableau:
    for e in sub:
        print(str(e).rjust(3), end=" ")
    print()