from safeType import *

#Input du nombre
nombre = safeInt(input("Votre Nombre: "))


if(nombre%11 == 0):
    print("Votre nombre est divisible par 11")
else:
    print("Votre nombre n'est pas divisible par 11")