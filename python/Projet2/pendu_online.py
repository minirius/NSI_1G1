import random
import os
from tkinter import Tk, font, StringVar, Canvas
from tkinter.ttk import Button, Label, Entry
import requests
import socket
import time
from threading import Thread

MOT = ""
ETAT = []
NBR_ERREUR = 0
LISTE_DEJA_FAIT = []
LISTE_DEJA_FAIT_TOTAL = []
WIN = False


LIST_PLAYER = []
ROOM = random.randint(0, 10000)
PLAYER = []

VARIANTE = {
    'A' : 'AÀÄÂÆ',
    'C' : 'CÇ',
    'E' : 'EÉÈÊËÆŒ',
    'I' : 'IÎÏ',
    'O' : 'OÔÖŒ',
    'U' : 'UÙÜÛ'
}

def updateAPI():
    response = requests.get("https://vibechat.fr/api/game_api.php?get")

def isPing():
    response = requests.get("https://vibechat.fr/api_jeux/game.php?get")
    index = 0
    selected = False
    for element in response.text.strip().split(';'):
        if(element != ""):
            if(elements[0] == IP):
                print("I WAS SELECTED")
                selected = True
    if(not selected): isPing()
            

def playerList():
    response = requests.get("https://vibechat.fr/api_jeux/listPlayer.php?get")
    index = 0
    for element in response.text.strip().split(';'):
        if(element != "" and element.split(":")[0] != IP):
            elements = element.split(":")
            print("["+str(index)+"] > ", elements[1], ":", elements[0])
            LIST_PLAYER.append(elements)
            index+=1

class App:
    def __init__(self, master):
        self.showvar = StringVar(master, " ".join(ETAT))
        self.errorvar = StringVar(master, "")
        self.infovar = StringVar(master, "Vous avez fait "+str(NBR_ERREUR)+" erreurs")
        self.dejafaitvar = StringVar(master, ", ".join(LISTE_DEJA_FAIT))

        self.label_big_font = font.Font(size=20)
        self.label_small_font = font.Font(size=12)
        self.button_font = font.Font(size=15)

        self.canvas = Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack(side="top")

        self.liste_label = Label(master, textvariable=self.dejafaitvar, font=self.label_small_font)
        self.liste_label.pack(side="bottom")
        
        self.info_label = Label(master, textvariable=self.infovar, font=self.label_small_font)
        self.info_label.pack(side="bottom")

        self.entry = Entry(master, text="Deviner !")
        self.entry.pack(side="bottom", pady=20)
        self.entry.bind('<Return>', self.update)

        self.display_label = Label(master, textvariable=self.showvar, font=self.label_big_font)
        self.display_label.pack(side="bottom")

        self.error_label = Label(master, textvariable=self.errorvar, font=self.label_small_font, foreground="#ff0000")
        self.error_label.pack(side="bottom")

    def update(self, e):
        global NBR_ERREUR, LISTE_DEJA_FAIT, WIN
        if(WIN): return
        if(NBR_ERREUR >= 10): return
        lettre = self.entry.get()
        lettre_etat = nouvel_etat(lettre)
        self.entry.delete(0, len(lettre))

        if(lettre == ""):
            self.errorvar.set("Veuillez entrer quelquechose !")
            return
        if(len(lettre) >= 2):
            self.errorvar.set("Veuillez entrer une lettre seulement !")
            return
        if(lettre.isdigit()):
            self.errorvar.set("Veuillez entrer un caractère valide !")
            return
        if(lettre in LISTE_DEJA_FAIT_TOTAL):
            self.errorvar.set("Veuillez entrer une nouvelle lettre !")
            return

        if(not lettre_etat[2]):
            NBR_ERREUR += 1
            LISTE_DEJA_FAIT.append(lettre)
            self.infovar.set("Vous avez fait "+str(NBR_ERREUR)+" erreurs")

        LISTE_DEJA_FAIT_TOTAL.append(lettre)
        self.errorvar.set("")
        self.showvar.set(" ".join(ETAT))
        self.entry.delete(0, len(lettre))
        self.dejafaitvar.set(", ".join(LISTE_DEJA_FAIT))
        self.draw()
        if(WIN):
            self.display_label.config(foreground="#009800")
            self.infovar.set("Gagné !")
        if(NBR_ERREUR >= 10): 
            self.infovar.set("Perdu !")
            self.display_label.config(foreground="#ff0000")
            self.showvar.set(" ".join(list(MOT)))
    
    def draw(self):
        global NBR_ERREUR, LISTE_DEJA_FAIT, WIN

        if(NBR_ERREUR == 1):
            self.canvas.create_line((50, 350), (350, 350), fill="black", width=5)
        if(NBR_ERREUR == 2):
            self.canvas.create_line((120, 350), (120, 50), fill="black", width=5)
        if(NBR_ERREUR == 3):
            self.canvas.create_line((120, 50), (300, 50), fill="black", width=5)
        if(NBR_ERREUR == 4):
            self.canvas.create_line((120, 90), (160, 50), fill="black", width=5)
        if(NBR_ERREUR == 5):
            self.canvas.create_line((300, 50), (300, 90), fill="black", width=5)
        if(NBR_ERREUR == 6):
            self.canvas.create_oval((275, 90), (325, 140), fill="white" ,width=5)
        if(NBR_ERREUR == 7):
            self.canvas.create_line((300, 140), (300, 230), fill="black", width=5)
        if(NBR_ERREUR == 8):
            self.canvas.create_line((300, 230), (275, 300), fill="black", width=5)
        if(NBR_ERREUR == 9):
            self.canvas.create_line((300, 230), (325, 300), fill="black", width=5)
        if(NBR_ERREUR == 10):
            self.canvas.create_line((250, 160), (350, 160), fill="black", width=5)

def nouvel_etat(lettre):
    global MOT, ETAT, WIN
    lettre = lettre.upper()
    lettres = [lettre]
    if(VARIANTE.get(lettre) != None):
        lettres = lettres+list(VARIANTE.get(lettre))
    didModified = False
    for index, element in enumerate(MOT):
        for i in lettres:
            if(element == i):
                ETAT[index] = i
                didModified = True
    if(MOT == "".join(ETAT)):
        WIN = True
    return MOT, ETAT, didModified, WIN

def selectionner_mot():
    global MOT, ETAT
    f = open("./python/Projet2/littre.txt","r", encoding="UTF-8")
    MOT = random.choice(f.readlines()).strip()
    ETAT = ["_" for i in MOT]
    return MOT, ETAT

def main():
    global WIN, LISTE_DEJA_FAIT, NBR_ERREUR, NAME, PLAYER, LIST_PLAYER, IP
    selectionner_mot()
    print(MOT)


    IP = socket.gethostbyname(socket.gethostname())
    print(IP)
    NAME = input("Votre nom: ")
    response = requests.get("https://vibechat.fr/api_jeux/listPlayer.php?add&name="+NAME+"&ip="+IP)


    playerList()
    selectedPlayer = int(input("-> "))
    PLAYER = LIST_PLAYER[selectedPlayer]
    print(PLAYER)

    response = requests.get("https://vibechat.fr/api_jeux/game.php?add&name="+NAME+"&ip="+IP+"&room="+str(ROOM)+"&word="+MOT+"&state="+"".join(ETAT))
    time.sleep(0.5)
    response = requests.get("https://vibechat.fr/api_jeux/game.php?add&name="+PLAYER[1]+"&ip="+PLAYER[0]+"&room="+str(ROOM)+"&word="+MOT+"&state="+"".join(ETAT))
    time.sleep(0.5)

    response = requests.get("https://vibechat.fr/api_jeux/listPlayer.php?remove&ip="+IP)
    time.sleep(0.5)
    response = requests.get("https://vibechat.fr/api_jeux/listPlayer.php?remove&ip="+PLAYER[0])
    time.sleep(0.5)

    root = Tk()
    root.minsize(400, 600)
    root.maxsize(400, 600)
    root.title("Pendu Graphique")
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    try:
        main()
    finally:
        response = requests.get("https://vibechat.fr/api_jeux/listPlayer.php?remove&ip="+IP)
        response = requests.get("https://vibechat.fr/api_jeux/game.php?remove&ip="+IP)