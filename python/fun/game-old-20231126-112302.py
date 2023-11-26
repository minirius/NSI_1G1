from turtle import *
import requests

#Taille du canva
taille = 30
couleur = "black"
timePlay = 0

grille = [["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"] for i in range(taille)]

def updateGrille():
    response = requests.get("https://vibechat.fr/api/game_api.php?get")
    grid = (response.text.strip()).split("/")
    for i, line in enumerate((response.text.strip()).split("/")):
        for j, item in enumerate((line.strip()).split(" ")):
            if(i<30): grille[i][j] = item

#Boucle d'affichage
def afficher():
    global timePlay
    clear()
    for a in range(taille**2):
        goto((a//taille)*20 - (taille/2)*20, (a%taille)*20 - (taille/2)*20)
        color("black", grille[a//taille][a%taille])
        stamp()
    goto(0, (taille/2)*20)
    write("Color: "+couleur+" / "+str(timePlay), move=False, align="center", font=("Arial", 20, "normal"))

def changeColor():
    global couleur
    couleur = textinput("Color", "Couleur de Base")

def decreaseTime():
    global timePlay
    timePlay -= 1
    afficher()
    if(timePlay > 0):
        ontimer(decreaseTime, 1000)

def clickHandle(x, y):
    global timePlay
    x, y = x+taille*10+10, y+taille*10+10
    if(x>600 or y>600 or x<0 or y<0):
        changeColor()
    else:
        if(timePlay == 0):
            caseX = int(((round(x/10)*10)-1)/20)
            caseY = int(((round(y/10)*10)-1)/20)
            response = requests.get("https://vibechat.fr/api/game_api.php?add&x="+str(caseX)+"&y="+str(caseY)+"&color="+couleur)
            if(response.text == "Done"):
                grille[caseX][caseY] = couleur
            else:
                raise("Error", "Server couldn't add the pixel")
            timePlay = 5
            afficher()
            ontimer(decreaseTime, 1000)

def autoUpdate():
    updateGrille()
    afficher()
    ontimer(autoUpdate, 800)

#Setup du tracer et afficher de la grille
tracer(False);shape("square");up()
autoUpdate()
afficher()

#Event hanlder de la souris
onscreenclick(clickHandle)
listen()
title("PixelWar")

mainloop()