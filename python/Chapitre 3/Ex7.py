from safeType import *

annee = safeInt(input("année: "))
if((annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)):
    print("Bisextile")
else:
    print("Pas Bisextile")