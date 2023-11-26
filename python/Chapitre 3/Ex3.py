from safeType import *

n = safeInt(input("Votre Nombre: "))

diviseur = []
for i in range(2, n//2 + 1):
    if(n % i == 0):
        diviseur.append(i)

if(len(diviseur) == 0):
    print("Votre nombre est premier, les diviseurs sont donc 1 et "+str(n))
else:
    for nbr in diviseur:
        print(nbr, end="; ")