from turtle import *
import requests

#Taille du canva
taille = 30
couleur = "black"

grille = [["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"] for i in range(taille)]

def updateGrille():
    response = requests.get("http://jkrowlings.rf.gd/?get")
    print(response.json())

#Boucle d'affichage
def afficher():
    for a in range(taille**2):
        goto((a//taille)*20 - (taille/2)*20, (a%taille)*20 - (taille/2)*20)
        color("black", grille[a//taille][a%taille])
        stamp()
    goto(0, (taille/2)*20)
    write("color : "+couleur, move=False, align="center", font=("Arial", 20, "normal"))

def changeColor():
    global couleur
    couleur = textinput("Color", "Couleur de Base")

def clickHandle(x, y):
    x, y = x+taille*10+10, y+taille*10+10
    if(x>600 or y>600 or x<0 or y<0):
        changeColor()
    else:
        caseX = int(((round(x/10)*10)-1)/20)
        caseY = int(((round(y/10)*10)-1)/20)
        grille[caseX][caseY] = couleur
        afficher()


#Setup du tracer et afficher de la grille
tracer(False);shape("square");up()
afficher()

#Event hanlder de la souris
onscreenclick(clickHandle)
updateGrille()
listen()
title("Color Game")
mainloop()