from safeType import *

annee = safeInt(input("année : "))
if annee % 4 == 0:
    if annee % 100 == 0:
        if annee % 400 == 0:
            print("Bisextile")
        else:
            print("Pas Bisextile")
    else:
        print("Bisextile")
else:
    print("Pas bisextile")