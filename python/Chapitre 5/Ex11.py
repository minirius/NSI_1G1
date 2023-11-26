from turtle import *

#Input des lignes
ligne = int(input("nbr de ligne: "))
colonne = int(input("nbr de colonne: "))

#Setup du tracer
tracer(False);shape("square");up()

#Boucle d'affichage
for a in range(colonne*ligne):
    goto((a//ligne)*20 - (colonne/2)*20, (a%ligne)*20 - (ligne/2)*20)
    if((a//ligne)%2 == 0 and (a%ligne)%2 == 0 or (a//ligne)%2 != 0 and (a%ligne)%2 != 0): color("black", "black")
    else: color('black', "")
    stamp()

mainloop()