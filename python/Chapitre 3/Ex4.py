from safeType import *
import math

print("Sous la forme ax^2 + bx + c = 0 :")
a = safeFloat(input("a: "))
b = safeFloat(input("b: "))
c = safeFloat(input("c: "))

delta = b*b - 4*a*c

if delta > 0.0:
    x1 = ((-b) + math.sqrt(delta)) / 2*a
    x2 = ((-b) - math.sqrt(delta)) / 2*a
    print("Les solutions sont : x1="+str(x1)+" et x2="+str(x2))
elif delta == 0.0:
    x = (-b) / 2*a
    print("La solution double est x="+str(x))
else:
    print("Votre equation n'a pas de solution réelle")