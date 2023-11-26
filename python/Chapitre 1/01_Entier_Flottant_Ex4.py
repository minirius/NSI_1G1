##module maths
import math

##Interface terminle
print("Veuillez entrer les coodonnées sous forme de x;y")
#input coordonnées de A
posA = input("Position de A: ").split(";")
#input coordonnées de B
posB = input("Position de B: ").split(";")
#conversion et obtention des coordonnées
Ax = int(posA[0])
Ay = int(posA[1])
Bx = int(posB[0])
By = int(posB[1])

#calcul de la distance
dist = math.sqrt((Bx-Ax)*(Bx-Ax)+(By-Ay)*(By-Ay))

print((Bx-Ax)*(Bx-Ax), (By-Ay)*(By-Ay))
print(dist)