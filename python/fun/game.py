#######################################################
# Name : Pixel War
# Author : Marius Nerantzakis
#
# Petit jeu de Guerre de pixel en multijoueur (sans identification de joueur)
#######################################################
import collections
from turtle import Turtle, clear, goto, stamp, write, ontimer, Screen, shape, up, tracer, color, textinput, onscreenclick, mainloop, listen, title
#from turtle import *
from tkinter import messagebox
import requests

#Definition de la taille du canva (à modifier sur le serveur par la suite)
taille = 30

textTurtle = Turtle(visible=False)

#Déficition des variables couleur est timePlay
couleur = "grey20"
timePlay = 0
winner = ""

#Définition du dictionnaire de couleur (association des couleurs francaise et couleur anglaise)
liste_couleur = {"jaune":"gold", "bleu":"RoyalBlue", "beige":"AntiqueWhite1", "gris":"DarkGrey", "violet":"BlueViolet", "vert":"green3", "cyan":"cyan2", "orange":"darkOrange", 'noir':"grey20", "magenta":"magenta1", "rose":"orchid1", 'rouge':"red2"}
#Reverse du dictionaire précédent
color_list = {v: k for k, v in liste_couleur.items()}
#Création de la grille de jeu
grille = [["white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"] for i in range(taille)]

def count_point():
    c = collections.Counter()
    for sublist in grille:
        c.update(sublist)
    return c.most_common()

def did_win():
    global winner
    did_win = False
    best = count_point()[0]
    if(best[0] == "white"):
        best = count_point()[1]
    if(round((best[1]/(30*30))*100, 1) >= 50.0):
        did_win = True
        winner = color_list[best[0]]
        textTurtle.clear()
        textTurtle.goto(-150, (taille/2)*20)
        textTurtle.write("Partie terminée, "+winner+" à gagné", move=False, align="center", font=("Arial", 20, "bold"))
        print("Gagné", best)
    
    return did_win

def search_for_events():
    for a in range(taille**2):
        x, y = a//taille, a%taille
        if(grille[x][y] == couleur):
            if(grille[x-1][y] == couleur and grille[x+1][y] == couleur and grille[x][y-1] == couleur and grille[x][y+1] == couleur):
                print("Etoile les gars")

#Fonction Update Grille, 
def updateGrille():
    changed = False
    response = requests.get("https://vibechat.fr/api/game_api.php?get")
    for i, line in enumerate((response.text.strip()).split("/")):
        for j, item in enumerate((line.strip()).split(" ")):
            if(i<30):
                if(grille[i][j] != item): 
                    changed = True
                    grille[i][j] = item
    return changed

#Boucle d'affichage
def afficher():
    global timePlay, textTurtle
    clear()
    textTurtle.clear()
    for a in range(taille**2):
        goto((a//taille)*20 - (taille/2)*20 - 150, (a%taille)*20 - (taille/2)*20)
        color("black", grille[a//taille][a%taille])
        stamp()
    textTurtle.goto(-150, (taille/2)*20)
    textTurtle.write("Color: "+color_list[couleur]+" / "+str(timePlay), move=False, align="center", font=("Arial", 20, "bold"))
    goto(170, (taille/2)*20)
    write("Tableau des Scores: ", move=False, align="left", font=("Arial", 20, "bold"))
    TableauScore = count_point()
    index=0
    for element in TableauScore:
        if(element[0] != "white"):
            goto(170, (taille/2)*20 - index*30 - 60)
            write(color_list[element[0]]+" : "+str(round((element[1]/(30*30))*100, 1))+"% ("+str(element[1])+" pixels )", move=False, align="left", font=("Arial", 20, "normal"))
            index+=1

def changeColor():
    global couleur, liste_couleur
    temp_couleur = textinput("Couleur", "Couleur du pixel (en francais)")
    if(type(temp_couleur) == type(None)):
        return
    temp_couleur = temp_couleur.lower()
    if(temp_couleur == "blanc"):
        messagebox.showwarning(message="Vous ne pouvez pas choisir le blanc !")
    elif not (temp_couleur in liste_couleur):
        messagebox.showwarning(message="Couleur non acceptée !")
    else:
        couleur =liste_couleur[temp_couleur]
        textTurtle.clear()
        textTurtle.goto(-150, (taille/2)*20)
        textTurtle.write("Color: "+color_list[couleur]+" / "+str(timePlay), move=False, align="center", font=("Arial", 20, "bold"))


def decreaseTime():
    global timePlay
    timePlay -= 1
    textTurtle.clear()
    textTurtle.goto(-150, (taille/2)*20)
    textTurtle.write("Color: "+color_list[couleur]+" / "+str(timePlay), move=False, align="center", font=("Arial", 20, "bold"))
    if(timePlay > 0):
        ontimer(decreaseTime, 1000)

def clickHandle(x, y):
    global timePlay
    x, y = x+taille*10+10 +150, y+taille*10+10
    if(x>600 or y>600 or x<0 or y<0):
        changeColor()
    else:
        if(timePlay == 0 and winner==""):
            caseX = int(((round(x/10)*10)-1)/20)
            caseY = int(((round(y/10)*10)-1)/20)
            if(grille[caseX][caseY] == 'white'):
                response = requests.get("https://vibechat.fr/api/game_api.php?add&x="+str(caseX)+"&y="+str(caseY)+"&color="+couleur)
                if(response.text == "Done"):
                    grille[caseX][caseY] = couleur
                else:
                    messagebox.showerror(title="Erreur Serveur, votre pixel n'a pas pu être placé !")
                timePlay = 3
                search_for_events()
                afficher()
                if not did_win():
                    ontimer(decreaseTime, 1000)

def autoUpdate():
    if updateGrille():
        did_win()
        afficher()
    ontimer(autoUpdate, 800)

screen = Screen()
screen.setup(taille*20+400, taille*20+70)
#Setup du tracer et afficher de la grille
tracer(False);shape("square");up()
textTurtle._tracer(False);textTurtle.shape("square");textTurtle.penup()
autoUpdate()
afficher()

#Event hanlder de la souris
onscreenclick(clickHandle)
listen()
title("PixelWar")

mainloop()